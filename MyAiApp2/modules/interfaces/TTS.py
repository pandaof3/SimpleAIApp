import abc
class ITTS:
    @abc.abstractmethod
    #should return a stream of bytes
    def Work(self,msg:str):
        pass