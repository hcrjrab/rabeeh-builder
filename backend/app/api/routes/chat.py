from fastapi import APIRouter

from app.schemas.chat import ChatRequest, ChatResponse
from app.services.ollama_service import ollama_service

router = APIRouter(
    prefix="/chat",
    tags=["Chat"],
)


@router.post("", response_model=ChatResponse)
async def chat(request: ChatRequest):
    answer = ollama_service.chat(request.message)

    return ChatResponse(
        success=True,
        response=answer,
    )