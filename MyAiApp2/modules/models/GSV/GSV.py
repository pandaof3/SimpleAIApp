from modules.models.GSV.TTSData import TTSData
import requests
class GSV():
    url = ""
    data = TTSData()
    headers = {"Content-Type":"application/json"}


    def SetUrl(self,url:str):
        self.url = url
    def SetText(self, text:str):
        self.data.SetText(text)
    def SetSpeed(self, speed:float):
        self.data.SetSpeed(speed)
    def SetTextLang(self, lang:str):
        self.data.SetTextLang(lang)
    def SetRefAudioPath(self,path:str):
        self.data.SetRefAudioPath(path)
    def SetPromptText(self, text:str):
        self.data.SetPromptText(text)
    def SetPromptLang(self,lang:str):
        self.data.SetPromptLang(lang)
    def Work(self,msg:str):
        self.SetText(msg)
        response = requests.post(self.url,json=self.data.GenerateData(),headers=self.headers)
        if response.status_code == 200:
            return response.content