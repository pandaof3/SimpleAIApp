from modules.interfaces.EstTokenCalculator import IEstTokenCalculator
class EstTokenCalcForEnglish(IEstTokenCalculator):
    def Calc(self,msg:str):
        return len(msg.split())+len(msg)//4