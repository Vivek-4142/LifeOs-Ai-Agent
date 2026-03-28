from fastapi import APIRouter
from app.models.request_models import UserRequest
from app.agents.orchestrator_agent import OrchestratorAgent

router = APIRouter()
orchestrator = OrchestratorAgent()


@router.get("/")
def health_check():
    return {"message": "Akaion Agentic Inbox Assistant is running"}


@router.post("/run")
def run_agent(request: UserRequest):
    return orchestrator.run(request.user_request)