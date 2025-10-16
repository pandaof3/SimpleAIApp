from modules.models.Ollama.OllamaLLM import OllamaLLM
from modules.models.GSV.GSV import GSV
from modules.view.AudioPlayer import AudioPlayer
import configparser
if __name__ == "__main__":
    config = configparser.ConfigParser()
    config.read("config.ini",encoding = 'utf-8')
    llm = OllamaLLM(config)
    tts = GSV(config)
    audio_player = AudioPlayer()
    while(True):
        newMsg = str(input())
        res = llm.Chat(newMsg)
        stream = tts.Work(res)
        print(res+"\n")
        audio_player.Play(stream)

        
