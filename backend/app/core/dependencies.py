from app.core.container import container


def get_chat_service():
    """
    Return ChatService instance.
    """
    return container.chat


def get_conversation_service():
    """
    Return ConversationService instance.
    """
    return container.conversation


def get_memory_service():
    """
    Return MemoryService instance.
    """
    return container.memory


def get_tool_service():
    """
    Return ToolService instance.
    """
    return container.tools