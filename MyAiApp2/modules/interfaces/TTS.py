import abc
import configparser
from logging import config
class ITTS:
    @abc.abstractmethod
    #should return a stream of bytes
    def Work(self,msg:str):
        pass
    @abc.abstractmethod
    def SetNecessities(self, config:configparser.ConfigParser):
        pass
    @abc.abstractmethod
    def SetOptions(self,config:configparser.ConfigParser):
        pass
    def __init__(self,config:configparser.ConfigParser):
        self.SetNecessities(config)
        self.SetOptions(config)