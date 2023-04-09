import json
from typing import List, Dict

import openai

from settings import SUPPORTED_MODELS


class NotSupportedModel(Exception):
    """Raised when the input model is not in the SUPPORTED_MODELS list"""
    pass


class ChatGPTSession:
    def __init__(self, model: str = "gpt-3.5-turbo"):
        self.messages = []
        if model not in SUPPORTED_MODELS:
            raise NotSupportedModel

        self.model = model

    async def new_message(self, message: str) -> str:
        self.messages.append(
            {"role": "user", "content": message}
        )
        response = await openai.ChatCompletion.acreate(
            model=self.model,
            messages=self.messages,
        )
        if response['choices'][0]['finish_reason'] == "stop":
            content = response['choices'][0]['message']['content']
            self.messages.append({"role": "assistant", "content": content})
        return content

    async def reset_messages(self):
        self.messages = []


class ChatServer:
    def __init__(self, org_name: str, api_key: str) -> None:
        self.chats = {}

        openai.api_key = api_key
        openai.organization = org_name

    async def create_chat(self, chat_id: int, model: str = "gpt-3.5-turbo") -> ChatGPTSession:
        chat = ChatGPTSession(model=model)
        self.chats[chat_id] = chat
        return chat
