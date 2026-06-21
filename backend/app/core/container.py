from app.services.chat_service import chat_service
from app.services.conversation_service import conversation_service
from app.memory.memory_service import memory_service
from app.services.tool_service import tool_service


class ServiceContainer:
    """
    Central container for all application services.
    """

    def __init__(self):
        self.chat = chat_service
        self.conversation = conversation_service
        self.memory = memory_service
        self.tools = tool_service


container = ServiceContainer()