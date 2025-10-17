import re
class TextSplitter():
    pattern = r'[,.!?;]+'

    def SplitText(self,text:str):
        sentences = re.split(self.pattern, text)
        return [s for s in sentences if s.strip()]