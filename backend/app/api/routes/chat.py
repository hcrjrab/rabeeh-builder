from fastapi import APIRouter

from app.schemas.chat import ChatRequest, ChatResponse
from app.services.chat_service import chat_service
from app.database.session import SessionLocal

router = APIRouter(
    prefix="/chat",
    tags=["Chat"],
)


@router.post(
    "",
    response_model=ChatResponse,
)
async def chat(request: ChatRequest):

    db = SessionLocal()

    try:

        answer = chat_service.send_message(
            db=db,
            conversation_id=request.conversation_id,
            message=request.message,
        )

        return ChatResponse(
            success=True,
            response=answer,
        )

    finally:
        db.close()