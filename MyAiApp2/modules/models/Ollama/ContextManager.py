from typing import List
from modules.models.Ollama.message import Message, MessageRole
from modules.utils.EstTokenCalcForEnglish import EstTokenCalcForEnglish
class ContextManager:
    def __init__(self, max_tokens:int = 4096, max_messages:int = 10):
        self.max_tokens = max_tokens
        self.max_messages = max_messages
        self.est_tokens = 0
        self.sys_msgs:List[Message] = []
        self.msgs:List[Message] = []
    def AddMessage(self,msg:str, role:MessageRole):
        newMsg = Message(msg, role, EstTokenCalcForEnglish())
        while(self.est_tokens+newMsg.est_tokens>self.max_tokens or len(self.msgs)>=self.max_messages):
            if not self.msgs:
                print("message too long")
                return
            removed_msg = self.msgs.pop(0)
            self.est_tokens-=removed_msg.est_tokens
        self.msgs.append(newMsg)
        self.est_tokens+=newMsg.est_tokens
    def ClearContext(self):
        for msg in self.msgs:
            self.est_tokens-=msg.est_tokens
        self.msgs.clear()
    def SetSystemMessage(self, sys_msg:str):
        newMsg = Message(sys_msg, MessageRole.SYSTEM, EstTokenCalcForEnglish())
        self.sys_msgs.append(newMsg)
        self.est_tokens+=newMsg.est_tokens
    def GenerateMessages(self):
        return [msg.to_dict() for msg in self.sys_msgs] + [msg.to_dict() for msg in self.msgs]