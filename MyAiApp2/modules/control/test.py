from modules.models.Ollama.OllamaLLM import OllamaLLM
from modules.models.GSV.GSV import GSV
from modules.view.AudioPlayer import AudioPlayer
import configparser
import re
if __name__ == "__main__":
    config = configparser.ConfigParser()
    config.read("config.ini",encoding = 'utf-8')
    llm = OllamaLLM()
    tts = GSV()
    tts.SetUrl(config["GSV"]["url"])
    tts.SetTextLang(config["GSV"]["text_lang"])
    tts.SetPromptLang(config["GSV"]["prompt_lang"])
    tts.SetPromptText(config["GSV"]["prompt_text"])
    tts.SetRefAudioPath(config["GSV"]["ref_audio_path"])

    tts.SetSpeed(config["GSVOptions"].getfloat("speed_factor"))
    audio_player = AudioPlayer()
    llm.SetUrl(config["Ollama"]["Ollama_url"])
    llm.SetModel(config["Ollama"]["Ollama_model"])
    llm.SetSysMsg(config["Ollama"]["system_message"])
    for key in config["OllamaOptions"]:
        if re.match(r'^\d+.\d+$', config["OllamaOptions"][key]):
            llm.SetOption(key, config["OllamaOptions"].getfloat(key))
    while(True):
        newMsg = str(input())
        res = llm.Chat(newMsg)
        stream = tts.Work(res)
        print(res+"\n")
        audio_player.Play(stream)

        
