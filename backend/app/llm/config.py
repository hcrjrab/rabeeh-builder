from pathlib import Path

import yaml


class LLMConfig:

    def __init__(self):

        config_path = Path(
            "backend/config/llm_config.yaml"
        )

        with open(
            config_path,
            "r",
            encoding="utf-8"
        ) as f:

            self.config = yaml.safe_load(f)

    @property
    def default_provider(self):

        return self.config["default_provider"]

    def provider(self, name: str):

        return self.config["providers"][name]

    def model(self, task: str):

        return self.config["models"][task]


llm_config = LLMConfig()