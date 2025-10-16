import abc
import configparser
from typing import List, Optional, Generic

class ILLM:
    @abc.abstractmethod
    def Chat(newMsg:str)->str:
        pass
    @abc.abstractmethod
    def SetOptions(config):   #设置可选选项
        pass
    @abc.abstractmethod
    def SetNecessities(config): #设置必要选项
        pass
    def __init__(self,config:configparser.ConfigParser):
        self.SetNecessities(config)
        self.SetOptions(config)