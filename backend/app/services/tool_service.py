class ToolService:
    """
    Future Tool Manager.
    """

    def get_available_tools(self):

        return [
            "calculator",
            "terminal",
            "file",
            "browser",
        ]


tool_service = ToolService()