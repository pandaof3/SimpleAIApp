from typing import TypeVar

T = TypeVar('T')

class TTSData:
    text:str = None
    text_lang = ""
    ref_audio_path = ""
    prompt_text = ""
    prompt_lang = ""
    speed_factor:float = None

    def SetText(self,text:str):
        self.text = text
    def SetSpeed(self,speed:float):
        self.speed_factor = speed
    def SetOptions(self,key:str, value:T):
        self.options[key] = value
    def SetTextLang(self,lang:str):
        self.text_lang = lang
    def SetRefAudioPath(self,path:str):
        self.ref_audio_path = path
    def SetPromptText(self, txt:str):
        self.prompt_text = txt;
    def SetPromptLang(self, lang):
        self.prompt_lang = lang
    def GenerateData(self):
        return {
            "text":self.text,
            "text_lang":self.text_lang,
            "ref_audio_path": self.ref_audio_path,
            "prompt_text":self.prompt_text,
            "prompt_lang":self.prompt_lang, 
            "speed_factor": self.speed_factor
        }