from datetime import datetime, timedelta
from typing import List, Optional
import os
print("Current working directory:", os.getcwd())
print("Templates folder exists:", os.path.exists("templates"))
from uuid import uuid4
from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel
from search_client import AzureSearchClient
from providers.cosmos.cosmos_provider import CosmosProvider
from dotenv import load_dotenv
from uuid import uuid4
from statistics import mean

load_dotenv()

router = APIRouter(tags=["Context"])

provider = CosmosProvider()  # <--- plug-in provider here

search_client = AzureSearchClient()

good_feedback_index = os.getenv("AZURE_SEARCH_GOOD_FEEDBACK_INDEX")
bad_feedback_index = os.getenv("AZURE_SEARCH_BAD_FEEDBACK_INDEX")

# --- Pydantic models ---
class EntityItem(BaseModel):
    Key: str
    Value: str

class SearchResultItem(BaseModel):
    id: str
    score: Optional[float] = None
    document: Optional[dict] = None

class FeedbackDocument(BaseModel):
    id: str
    Reason: Optional[str] = None
    AgentCode: Optional[str] = None
    Intent: Optional[str] = None
    Entity: Optional[List[EntityItem]] = None
    Content: Optional[str] = None
    CreatedOn: Optional[str] = None
    ModifiedOn: Optional[str] = None
    CreatedBy: Optional[str] = None
    ModifiedBy: Optional[str] = None

class ContextDocument(BaseModel):
    id: str
    PromptCode: Optional[str] = None
    ParentPromptCode: Optional[str] = None
    AgentCode: Optional[str] = None
    Content: Optional[str] = None
    Type: Optional[str] = None
    Intent: Optional[str] = None
    Default: Optional[bool] = False
    Approved: Optional[bool] = False
    VersionId: Optional[str] = None
    ContextVersion: Optional[str] = None
    Entity: Optional[List[EntityItem]] = None
    Latest: Optional[bool] = None
    CreatedOn: Optional[str] = None
    ModifiedOn: Optional[str] = None
    CreatedBy: Optional[str] = None
    ModifiedBy: Optional[str] = None

@router.get("/stats/contexts/count")
def get_contexts_count():
    """Get total count of all contexts using wildcard search."""
    try:
        results = search_client.search(agent_code="*", q="*", top=1000)
        return {"count": len(results)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/context-code/{context_code}/contexts")
def get_contexts_by_context_code_count(context_code: str):
    """Get total count of all contexts using wildcard search."""
    try:
        if not context_code or context_code.strip() == "":
            raise HTTPException(
                status_code=400,
                detail="context_code cannot be empty."
            )

        results = search_client.search_prompts_by_context_code(
            context_code=context_code,
            vector_search=False,
            user_msg=None,
            top=5
        )
        return {"results": results}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/stats/memories/count")
def get_memories_count():
    """Get total count of all memories."""
    try:
        # Search all memories with wildcard
        # Adjust this based on your memory storage implementation
        results = search_client.search(agent_code="*", q="*", top=10000)
        # Filter only memory-type documents if needed
        memory_results = [r for r in results if r.get('document', {}).get('Type') == 'memory']
        return {"count": len(memory_results)}
    except Exception as e:
        return {"count": 0}

@router.get("/stats/sessions/count")
def get_active_sessions_count():
    """Get count of active sessions for current date from Cosmos DB."""
    try:
        current_date = datetime.utcnow().strftime("%Y-%m-%d")
        # Query Cosmos DB for today's sessions
        # You'll need to implement get_sessions_by_date in your cosmos.py
        # For now, returning a placeholder
        # sessions = get_sessions_by_date(datetime.utcnow())
        return {"count": 0}  # Update this when you implement session counting
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/stats/audit/count")
def get_audit_logs_count():
    """Get count of audit logs from last 30 minutes."""
    try:
        target_datetime = datetime.utcnow() - timedelta(minutes=30)
        logs = provider.get_audit_logs_since(target_datetime)
        return {"count": len(logs) if logs else 0}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))    

@router.get("/agent-metrics", response_model=List[dict])
def fetch_agent_metrics(
    agent_code: Optional[str] = Query(None, description="AgentCode to filter metrics"),
    intent_code: Optional[str] = Query(None, description="IntentCode to filter metrics"),
    metric_code: Optional[str] = Query(None, description="MetricCode to filter metrics"),
    start_time: str = Query(..., description="Start UTC datetime in ISO format (e.g., 2025-10-27T00:00:00Z)"),
    end_time: str = Query(..., description="End UTC datetime in ISO format (e.g., 2025-10-27T23:59:59Z)"),
    min_value: Optional[float] = Query(None, description="Minimum metric value to filter"),
    max_value: Optional[float] = Query(None, description="Maximum metric value to filter")
):
    """
    Endpoint to retrieve agent metrics from the AgentMetrics container using either AgentCode or IntentCode (or both),
    within a specified datetime range. 
    If metric_code == 'cost', sum metric_value.
    If metric_code == 'performance', average metric_value.
    """
    try:
        metrics = provider.get_agent_metrics(
            agent_code=agent_code,
            intent_code=intent_code,
            metric_code=metric_code,
            start_time=start_time,
            end_time=end_time
        )

        # Safety check
        if not metrics:
            return []
        
        if min_value is not None or max_value is not None:
            filtered_metrics = []
            for m in metrics:
                val = m.get("MetricValue") or m.get("metricvalue") or m.get("metric_value")
                try:
                    val = float(val)
                    if (min_value is None or val >= min_value) and (max_value is None or val <= max_value):
                        filtered_metrics.routerend(m)
                except (TypeError, ValueError):
                    continue
            metrics = filtered_metrics

        # Handle aggregation logic
        if metric_code and metric_code.lower() == "cost":
            total_cost = 0
            for m in metrics:
                val = (
                    m.get("MetricValue")
                    or m.get("metricvalue")
                    or m.get("metric_value")
                    or 0
                )
                try:
                    val = float(val)
                except (TypeError, ValueError):
                    val = 0
                total_cost += val

            return [{
                "MetricCode": "COST",
                "TotalCost": total_cost,
                "Metrics": metrics
            }]
        
        elif metric_code and metric_code.lower() == "performance":
            values = [
                        float(m.get("MetricValue", 0))
                        for m in metrics
                        if m.get("MetricValue") not in (None, "") and (m.get("IntentCode") in (None, ""))
                    ]

            avg_performance = mean(values) if values else 0
            return [{"MetricCode": "PERFORMANCE", "average_performance": avg_performance, "Metrics": metrics}]

        # Default: return raw metrics
        return metrics

    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")

@router.post("/contexts", response_model=dict)
def create_documents(docs: List[ContextDocument]):
    """Create / upload multiple documents to the index."""
    try:
        docs = routerly_timestamps(docs)
        res = search_client.upload_documents([d.dict() for d in docs])
        return {"uploaded": res}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/good-feedback/contexts", response_model=dict)
def create_feedback_documents(docs: List[FeedbackDocument]):
    """Create / upload multiple documents to the index."""
    try:
        docs = routerly_timestamps(docs)
        res = search_client.upload_feedback_documents([d.dict() for d in docs], good_feedback_index)
        return {"uploaded": res}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/bad-feedback/contexts", response_model=dict)
def create_feedback_documents(docs: List[FeedbackDocument]):
    """Create / upload multiple documents to the index."""
    try:
        docs = routerly_timestamps(docs)
        res = search_client.upload_feedback_documents([d.dict() for d in docs], bad_feedback_index)
        return {"uploaded": res}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/agents/{agent_code}/contexts", response_model=List[ContextDocument])
def get_documents_by_agent(agent_code: str):
    """Retrieve all documents for a given agent_code."""
    try:
        docs = search_client.get_documents_by_agent(agent_code)
        return docs
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
 
@router.get("/context-code/{context_code}/contexts", response_model=List[ContextDocument])
def get_documents_by_context_code(context_code: str):
    """Retrieve all documents for a given agent_code."""
    try:
        docs = search_client.get_documents_by_context(context_code)
        return docs
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Helper method to place audit timestamps properly.
def routerly_timestamps(docs: List[ContextDocument]) -> List[ContextDocument]:
    """Inject CreatedOn and ModifiedOn into each ContextDocument."""
    utc_now = datetime.utcnow().isoformat() + "Z"  # Azure-compatible
    
    for doc in docs:
        doc.CreatedOn = utc_now
        doc.ModifiedOn = utc_now
    
    return docs

@router.get("/agent-code/{agent_code}/feedback-type/{feedback_type}/feedback-contexts", response_model=List[FeedbackDocument])
def get_feedback_context_by_agent_code(agent_code: str, feedback_type: str):
    """Retrieve all documents for a given agent_code."""
    try:
        if feedback_type == "good":
            index = good_feedback_index
        else:
            index = bad_feedback_index
        docs = search_client.search_feedback_contexts_by_agent(agent_code, False, None, index)
        return docs
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
 
@router.get("/contexts/{context_id}", response_model=ContextDocument)
def get_document(doc_id: str):
    """Retrieve a single document by id."""
    try:
        doc = search_client.get_document(doc_id)
        if not doc:
            raise HTTPException(status_code=404, detail="Document not found")
        return doc
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.get("/contexts/feedback/{doc_id}/feedback-type/{feedback_type}", response_model=FeedbackDocument)
def get_feedback_document(doc_id: str, feedback_type: str):
    """Get a single feedback document by ID."""
    try:
        if feedback_type == "good":
            index = good_feedback_index
        else:
            index = bad_feedback_index

        doc = search_client.get_feedback_document(doc_id, index)
        return doc

    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Document not found: {e}")

 
@router.put("/contexts/{context_id}", response_model=dict)
def update_document(doc_id: str, payload: ContextDocument, update_context_version: bool = False):
    """Update document by id (full replace)."""
    try:
        new_id = None
        body = payload.dict()
        body["id"] = doc_id
        body["ModifiedOn"] = datetime.utcnow().isoformat() + "Z"
        if update_context_version == True:
          new_id = str(uuid4())
        res = search_client.update_documents([body], doc_id, new_id)
        return {"updated": res}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))    

@router.get("/stats/contexts/count")
def get_contexts_count():
    """Get total count of all contexts using wildcard search."""
    try:
        results = search_client.search(agent_code="*", q="*", top=1000)
        return {"count": len(results)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/stats/memories/count")
def get_memories_count():
    """Get total count of all memories."""
    try:
        results = search_client.search(agent_code="*", q="*", top=10000)
        memory_results = [r for r in results if r.get('document', {}).get('Type') == 'memory']
        return {"count": len(memory_results)}
    except Exception as e:
        return {"count": 0}
    
@router.delete("/contexts/{context_id}", response_model=dict)
def delete_document(doc_id: str):
    """Delete document by id."""
    try:
        res = search_client.delete_document(doc_id)
        return {"deleted": res}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 

@router.delete("/contexts/feedback/{doc_id}/feedback-type/{feedback_type}", response_model=dict)
def delete_feedback_document(doc_id: str, feedback_type: str):
    try:
        if feedback_type == "good":
            res = search_client.delete_good_feedback_document(doc_id=doc_id)
        elif feedback_type == "bad":
            res = search_client.delete_bad_feedback_document(doc_id=doc_id)
        return {"deleted": res}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put("/contexts/feedback/{doc_id}/feedback-type/{feedback_type}", response_model=dict)
def update_feedback_document(
    doc_id: str,
    payload: FeedbackDocument,
    feedback_type: str
):
    """Update feedback document by id."""
    try:
        body = payload.dict()
        body["id"] = doc_id
        body["ModifiedOn"] = datetime.utcnow().isoformat() + "Z"
        res = search_client.update_feedback_document(body, feedback_index_type=feedback_type)
        return {"updated": res}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    
@router.get("/search", response_model=List[SearchResultItem])
def search(agent_code: str, version_id: Optional[str] = None, q: Optional[str] = None, top: int = 10):
    """Search documents filtered by agent_code and optionally version_id. `q` is a simple search text.
    This endpoint returns matching documents with score and the document content.
    """
    try:
        results = search_client.search(agent_code=agent_code, version_id=version_id, q=q, top=top)
        return results
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
   
@router.get("/logs", response_model=List[SearchResultItem])
def search(agent_code: str, version_id: Optional[str] = None, q: Optional[str] = None, top: int = 10):
    """Search documents filtered by agent_code and optionally version_id. `q` is a simple search text.
    This endpoint returns matching documents with score and the document content.
    """
    try:
        results = search_client.search(agent_code=agent_code, version_id=version_id, q=q, top=top)
        return results
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

