import abc
import configparser
from typing import List, Optional, Generic

class ILLM:
    @abc.abstractmethod
    def Chat(newMsg:str)->str:
        pass
    @abc.abstractmethod
    def SetOptions(config):   #���ÿ�ѡѡ��
        pass
    @abc.abstractmethod
    def SetNecessities(config): #���ñ�Ҫѡ��
        pass
    def __init__(self,config:configparser.ConfigParser):
        self.SetNecessities(config)
        self.SetOptions(config)