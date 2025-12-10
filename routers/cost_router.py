import os
print("Current working directory:", os.getcwd())
print("Templates folder exists:", os.path.exists("templates"))
from uuid import uuid4
from fastapi import APIRouter, HTTPException, Query
from providers.cosmos.cosmos_provider import CosmosProvider

from dotenv import load_dotenv

load_dotenv()

router = APIRouter(tags=["CostControl"])

provider = CosmosProvider()  # <--- plug-in provider here

@router.post("/agent-code/{agent_code}/resolve-agent-cost")
async def create_documents(agent_code: str):
    """Resolve cost policy for agents."""
    try:
        res = await provider.resolve_agent_violations(agent_code=agent_code)
        return {"uploaded": res}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.get("/aggregated-agent-monthly-cost")
async def aggregated_cost():
    """Resolve cost policy for agents."""
    try:
        res = await provider.retrieve_aggregated_costs()
        return {"uploaded": res}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.get("/agent-violated-cost")
async def violated_cost():
    """Resolve cost policy for agents."""
    try:
        res = await provider.retrieve_agent_violations()
        return {"uploaded": res}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.get("/monthly-user-agent-cost")
async def retrieve_monthly_cost():
    """Resolve cost policy for agents."""
    try:
        res = await provider.retrieve_monthly_costs()
        return {"monthly_costs": res}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

