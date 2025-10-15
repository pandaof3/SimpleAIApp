from typing import TypeVar

T = TypeVar('T')

class TTSData:
    text:str = None
    text_lang = "en"
    ref_audio_path = "D:/code/AI/GPT-SoVITS-v3lora-20250228/neuro/1.wav"
    prompt_text = "You want me to get rid of that chat member? There are ten thousand other ways to teach you a lesson!"
    prompt_lang = "en"
    speed_factor = 0.95

    def SetText(self,text:str):
        self.text = text
    def SetSpeed(self,speed:float):
        self.speed_factor = speed
    def SetOptions(self,key:str, value:T):
        self.options[key] = value
    def GenerateData(self):
        return {
            "text":self.text,
            "text_lang":self.text_lang,
            "ref_audio_path": self.ref_audio_path,
            "prompt_text":self.prompt_text,
            "prompt_lang":self.prompt_lang, 
            "speed_factor": self.speed_factor
        }