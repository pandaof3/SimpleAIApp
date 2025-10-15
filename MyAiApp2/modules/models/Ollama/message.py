from enum import Enum
from modules.interfaces.EstTokenCalculator import IEstTokenCalculator
class MessageRole(Enum):
    USER = "user"
    SYSTEM = "system"
    ASSISTANT = "assistant"

class Message:
    def __init__(self, content:str, role:MessageRole, calculator:IEstTokenCalculator):
        self.content = content
        self.role = role
        self.calculator = calculator
        self.est_tokens = calculator.Calc(content)

    def to_dict(self)->dict:
        return {"role" : self.role.value, "content": self.content}