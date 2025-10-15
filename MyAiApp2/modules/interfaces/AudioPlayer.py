from abc import ABC, abstractmethod

class IAudioPlayer():
    def Play(self, content:bytes):
        pass