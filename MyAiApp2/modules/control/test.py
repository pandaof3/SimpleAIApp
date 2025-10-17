from time import sleep
from typing import Text
from modules.interfaces.TTS import ITTS
from modules.models.Ollama.OllamaLLM import OllamaLLM
from modules.models.GSV.GSV import GSV
from modules.view.AudioPlayer import AudioPlayer
from modules.utils.TextSplitter import TextSplitter
import queue
import threading
import configparser

def AsyncTTS(tts:ITTS,audio_player:AudioPlayer, SQueue:queue.Queue,AudioQueue:queue.Queue):
    while not SQueue.empty():
        AudioQueue.put(tts.Work(SQueue.get()))
        thread1 = threading.Thread(target=AsyncPlayAudio,args=(audio_player,AudioQueue))
        thread1.start()
    return;

def AsyncPlayAudio(audio_player:AudioPlayer,AudioQueue:queue.Queue):
    while audio_player.Playing():
        sleep(0.1)
    audio_player.Play(AudioQueue.get())
    return;

if __name__ == "__main__":
    config = configparser.ConfigParser()
    config.read("config.ini",encoding = 'utf-8')
    llm = OllamaLLM(config)
    tts = GSV(config)
    audio_player = AudioPlayer()
    text_splitter = TextSplitter()
    while(True):
        newMsg = str(input())
        res = llm.Chat(newMsg)
        sentences = TextSplitter().SplitText(res)
        SQueue = queue.Queue()
        for sentence in sentences:
            SQueue.put(sentence)
        AudioQueue = queue.Queue()
        print(res+"\n")
        thread = threading.Thread(target=AsyncTTS,args=(tts,audio_player, SQueue,AudioQueue))
        thread.start()
        thread.join()
        

        
