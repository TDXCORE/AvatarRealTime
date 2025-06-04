from fastapi import APIRouter
from fastapi import Body, Depends
from backend.app.api.dependencies import get_current_user

router = APIRouter()

# Aquí irán los endpoints de agentes IA 

@router.post("/converse")
def converse_agent(message: str = Body(..., embed=True), user=Depends(get_current_user)):
    # Aquí se integrará LangChain/LangGraph
    return {"response": f"Agente responde a: {message}", "user": user}
