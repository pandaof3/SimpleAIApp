from modules.interfaces.LLM import ILLM
from modules.models.Ollama.ContextManager import ContextManager
from typing import TypeVar
import requests

from modules.models.Ollama.message import MessageRole
T = TypeVar('T')
class OllamaLLM(ILLM):
    url:str = ""
    model:str = ""
    stream:bool = False
    options:dict = {}
    contextmanager = ContextManager()

    def SetUrl(self, url:str):
        self.url = url
    def SetModel(self, model:str):
        self.model = model
    def SetStream(self, stream:bool):
        self.stream = stream
    def SetOption(self, key:str, value:T):
        self.options[key] = value
    def RemoveOption(self, key:str):
        self.options.pop(key, 0)
    def SetSysMsg(self, msg:str):
        self.contextmanager.SetSystemMessage(msg)
    def GeneratePayload(self):
        return {
            "model": self.model,
            "messages": self.contextmanager.GenerateMessages(),
            "stream": self.stream,
            "options": self.options
        }
    def Chat(self, msg:str)->str:
        self.contextmanager.AddMessage(msg,MessageRole.USER)
        response = requests.post(self.url, json = self.GeneratePayload())
        res_msg: str = response.json()["message"]["content"]
        self.contextmanager.AddMessage(res_msg, MessageRole.ASSISTANT)
        return res_msg
        