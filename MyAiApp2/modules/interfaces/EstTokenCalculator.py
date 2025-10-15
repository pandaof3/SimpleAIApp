import abc
class IEstTokenCalculator:
    @abc.abstractmethod
    def Calc(self, msg:str)->int :
        pass