from modules.interfaces.LLM import ILLM
from modules.models.Ollama.ContextManager import ContextManager
from typing import TypeVar
import requests
import configparser
from modules.models.Ollama.message import MessageRole
from modules.utils.ConfigReader import ConfigReader
T = TypeVar('T')
class OllamaLLM(ILLM):
    url:str = ""
    model:str = ""
    stream:bool = False
    options:dict = {}
    contextmanager = ContextManager()
    
    def __init__(self, config):
        self.configReader = ConfigReader(config)
        self.SetNecessities(config)
        self.SetOptions(config)
    def SetNecessities(self,config:configparser.ConfigParser):
        self.url = config["Ollama"]["Ollama_url"]
        self.model = config["Ollama"]["Ollama_model"]
        if config["Ollama"]["system_message"] != "":
            self.contextmanager.SetSystemMessage(config["Ollama"]["system_message"])
        self.stream = config["Ollama"].getboolean("stream")
    def SetOptions(self,config:configparser.ConfigParser):
        for keys in config["OllamaOptions"]:
            value = self.configReader.ReadByKey("OllamaOptions",keys)
            if value is not None:
                self.SetOption(keys,value)

    def SetOption(self, key:str, value:T):
        self.options[key] = value
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
        