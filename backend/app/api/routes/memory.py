from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.memory.memory_service import memory_service
from app.schemas.memory import (
    ConversationCreate,
    ConversationResponse,
    MessageResponse,
)

router = APIRouter(
    prefix="/memory",
    tags=["Memory"],
)


@router.post(
    "/conversation",
    response_model=ConversationResponse,
)
def create_conversation(
    request: ConversationCreate,
    db: Session = Depends(get_db),
):
    return memory_service.create_conversation(
        db,
        request.title,
    )


@router.get(
    "/conversation/{conversation_id}",
    response_model=list[MessageResponse],
)
def get_messages(
    conversation_id: int,
    db: Session = Depends(get_db),
):
    return memory_service.get_messages(
        db,
        conversation_id,
    )