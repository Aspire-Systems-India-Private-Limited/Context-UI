import json
import uuid
from fastapi import APIRouter
from managers.agent_manager import AgentManager
from managers.agent_solution_manager import AgentSolutionManager
from agent_model import AgentSolution, BaseAgent, UpdateAgentSolution
from typing import List
from fastapi import APIRouter, UploadFile, File, Form

router = APIRouter(prefix="/agent-solutions", tags=["Agent Solutions"])

@router.post("/", response_model=dict)
async def add_agent_solution(
    name: str = Form(...),
    permission_scopes: str = Form(...),  # JSON string
    url: str = Form(...),
    support_email: str = Form(...),
    description:str =Form(...),
    support_phone: str = Form(...),
    file: UploadFile = File(None)  # <-- file input in Swagger
        ):
    permission_scopes_list = permission_scopes.split(",")
    solution_data = AgentSolution(
        id=str(uuid.uuid4()),
        name=name,
        description=description,
        support={"email": support_email, "phone": support_phone},
        # permission_scopes=json.loads(permission_scopes),
        permission_scopes=permission_scopes_list,
        url=url,
        thumbnail=None  # will be set after upload
    )
    if file:
        image_bytes = await file.read()
        solution_data.thumbnail = AgentSolutionManager.upload_image(image_bytes)  
        return AgentSolutionManager.create_agent_solution(solution_data)
        
# @router.post("/", response_model=dict)
# def create_agent_solution(agent_solution: AgentSolution):
#     return AgentSolutionManager.create_agent_solution(agent_solution)

@router.get("/", response_model=list)
def list_agent_solutions():
    return AgentSolutionManager.list_agent_solutions()

@router.get("/{id}/agents", response_model=list)
def get_agents_by_solution(id: str):
    return AgentManager.get_agents_by_solution(id)

@router.put("/{id}")
def update_agent_solution(id: str, payload: UpdateAgentSolution):
        return AgentSolutionManager.update_agent_solution(id,payload)
    
@router.put("/{id}/image")
async def update_agent_solution_image(id: str, file: UploadFile = File(...)):
        file_bytes = await file.read()
        return AgentSolutionManager.update_solution_thumbnail(id,file_bytes)
    
@router.put("/{id}/description")
def update_agent_solution_description(id: str, description: str):
        return AgentSolutionManager.update_agent_solution_description(id,description)
    
@router.delete("/{id}")
def delete_agent_solution_description(id: str):
        return AgentSolutionManager.soft_delete_agent(id)
    

