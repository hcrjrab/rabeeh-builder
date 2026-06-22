class ModelSelector:
    """
    Selects the best model for each task.
    """

    def __init__(self):

        self.models = {

            "chat": {
                "provider": "ollama",
                "model": "llama3.1"
            },

            "coding": {
                "provider": "ollama",
                "model": "qwen2.5-coder"
            },

            "reasoning": {
                "provider": "ollama",
                "model": "deepseek-r1"
            },

            "vision": {
                "provider": "ollama",
                "model": "llava"
            }

        }

    def select(
        self,
        task: str = "chat",
    ) -> dict:

        return self.models.get(
            task,
            self.models["chat"]
        )


model_selector = ModelSelector()