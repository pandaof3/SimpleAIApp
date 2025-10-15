import abc
from typing import List, Optional, Generic

class ILLM:
    @abc.abstractmethod
    def Chat(newMsg:str)->str:
        pass