from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.memory.memory_service import memory_service
from app.schemas.chat import ChatRequest, ChatResponse
from app.services.agent_service import agent_service

router = APIRouter(
    prefix="/chat",
    tags=["Chat"],
)


@router.post("", response_model=ChatResponse)
async def chat(
    request: ChatRequest,
    db: Session = Depends(get_db),
):
    # Save user message
    memory_service.save_message(
        db=db,
        conversation_id=request.conversation_id,
        role="user",
        content=request.message,
    )

    # Generate AI response
    answer = agent_service.chat(
        db=db,
        conversation_id=request.conversation_id,
        message=request.message,
    )

    # Save assistant response
    memory_service.save_message(
        db=db,
        conversation_id=request.conversation_id,
        role="assistant",
        content=answer,
    )

    return ChatResponse(
        success=True,
        response=answer,
    )