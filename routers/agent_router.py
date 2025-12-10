from fastapi import APIRouter, Query,HTTPException,status
from typing import List, Optional
from agent_model import Agent,BaseAgent,AgentConfig
from managers.agent_manager import AgentManager
from pydantic import BaseModel,Field
from fastapi.responses import FileResponse
from fastapi.templating import Jinja2Templates

router = APIRouter(prefix="/agents", tags=["Agents"])

templates = Jinja2Templates(directory="AGENT-OPS/templates")

@router.post("/", response_model=dict)
def create_agent(agent: Agent):
    return AgentManager.create_agent(agent)

@router.get("/", response_model=list)
def list_agents(name: Optional[str] = Query(None, description="Filter by name"),
    status: Optional[str] = Query(None, description="Filter by status"),
    provider: Optional[str] = Query(None, description="Filter by provider"),
    code: Optional[str] = Query(None, description="Filter by Agent Code"),
    environment:Optional[str] = Query(None, description="Filter by Agent Code"),
    category: Optional[str] = Query(None, description="Filter by Category (comma-separated)")):
        print(f"Received -> name={name}, status={status}, provider={provider}, code={code}, environment={environment}")
        agents = AgentManager.list_agents(name, status, provider, code, environment,category)

        for agent in agents:
            if "category" in agent and isinstance(agent["category"], list):
                agent["category"] = ", ".join(agent["category"])

        return agents

@router.get("/{agent_id}", response_model=dict)
def get_agent(agent_id: str):
    return AgentManager.get_agent(agent_id)

@router.get("/by_code/{agent_code}", response_model=dict)
def get_agent_by_code(agent_code: str):
    return AgentManager.get_agent_by_code(agent_code)
@router.delete("/{agent_id}",response_model=dict)
def delete_agent(agent_id: str):
    return AgentManager.soft_delete_agent(agent_id)

@router.put("/{agent_id}", response_model=dict)
def update_agent(agent_id: str, agent: Agent):
    return AgentManager.update_agent(agent_id, agent)

@router.post(
    "/{agent_id}/config",
    response_model=dict,
    status_code=status.HTTP_201_CREATED
)
def create_agent_config(agent_id: str, config: AgentConfig):

    allowed_types = ["rbac", "cost", "model_routing", "data_scope"]

    # ✅ This is correct now: uses config.config_type
    if config.config_type not in allowed_types: 
        raise HTTPException(
            status_code=400, 
            detail=f"Invalid config_type : {config.config_type}"
        )
    agent_details = AgentManager.get_agent_by_code(config.agent_code)

    if not agent_details:
        raise HTTPException(
            status_code=404, 
            detail=f"Agent with code '{config.agent_code}' not found."
        )

    actual_agent_id = agent_details.get("id")    

    return AgentManager.add_config(
        agent_id=actual_agent_id,
        version=config.version,
        agent_code=config.agent_code,
        config_type=config.config_type, 
        data=config.data
    )
@router.get("/{agent_code}/config/{config_type}", response_model=list)
def list_agent_configs(agent_code: str, config_type: str):
    allowed_types = ["rbac", "cost", "model_routing", "data_scope"]

    if config_type not in allowed_types:
        raise HTTPException(400, f"Invalid config_type: {config_type}")

    agent = AgentManager.get_agent_by_code(agent_code)
    if not agent:
        raise HTTPException(404, "Agent not found")

    # Extract agent_id from agent document
    agent_id = agent.get("id")

    # Step 2: Fetch configs using agent_id
    return AgentManager.list_configs(agent_id, config_type)


@router.get("/config/{config_id}", response_model=dict)
def get_config_by_id(config_id: str):
    """
    Fetch a single config by its unique config ID.
    """
    config = AgentManager.get_config_by_id(config_id)

    if not config:
        raise HTTPException(
            status_code=404,
            detail=f"Config with ID '{config_id}' not found"
        )

    return config 
@router.get("/{agent_id}/view-configs")
def view_configs_page(agent_id: str):
    return FileResponse("templates/view_configs.html")
# @router.delete("/{agent_id}", response_model=dict)
# def delete_agent(agent_id: str):
#    return AgentManager.delete_agent(agent_id)
