from ssl import Options
from typing import TypeVar
from modules.utils.ConfigReader import ConfigReader
import configparser
import json

T = TypeVar('T')

class GSVData:
    text:str = None
    text_lang = ""
    ref_audio_path = ""
    prompt_text = ""
    prompt_lang = ""
    options:dict = {}

    def SetNecessities(self,config:configparser.ConfigParser):
        config_reader = ConfigReader(config)
        self.text_lang = config_reader.ReadByKey("GSV","text_lang")
        self.ref_audio_path = config_reader.ReadByKey("GSV","ref_audio_path")
        self.prompt_text = config_reader.ReadByKey("GSV","prompt_text")
        self.prompt_lang = config_reader.ReadByKey("GSV","prompt_lang")
    def SetOptions(self,config:configparser.ConfigParser):
        config_reader = ConfigReader(config)
        for keys in config["GSVOptions"]:
            value = config_reader.ReadByKey("GSVOptions",keys)
            if value is not None:
                self.SetOption(keys,value)
    def SetOption(self,key:str, value:T):
        self.options[key] = value
    def SetText(self,text:str):
        self.text = text
    def GenerateData(self):
        dict1 = {
            "text":self.text,
            "text_lang":self.text_lang,
            "ref_audio_path": self.ref_audio_path,
            "prompt_text":self.prompt_text,
            "prompt_lang":self.prompt_lang
            }
        result = {**dict1, **self.options}
        return result
            
        