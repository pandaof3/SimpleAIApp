from modules.models.GSV.GSVData import GSVData
from modules.interfaces.TTS import ITTS
import requests
class GSV(ITTS):
    url = ""
    data = GSVData()
    headers = {"Content-Type":"application/json"}
    def SetNecessities(self, config):
        self.url = config["GSV"]["url"]
        self.data.SetNecessities(config)
    def SetOptions(self, config):
        self.data.SetOptions(config)
    def SetText(self, text:str):
        self.data.SetText(text)
    def Work(self,msg:str):
        self.SetText(msg)
        response = requests.post(self.url,json=self.data.GenerateData(),headers=self.headers)
        if response.status_code == 200:
            return response.content