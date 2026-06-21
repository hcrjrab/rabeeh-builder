from pydantic import BaseModel


class ConversationCreate(BaseModel):
    title: str = "New Chat"


class ConversationResponse(BaseModel):
    id: int
    title: str

    model_config = {
        "from_attributes": True
    }


class MessageResponse(BaseModel):
    id: int
    role: str
    content: str

    model_config = {
        "from_attributes": True
    }