import pyaudio
import wave
import io
from time import sleep
from modules.interfaces.AudioPlayer import IAudioPlayer
class AudioPlayer(IAudioPlayer):

    is_playing = False
    def Playing(self) -> bool:
        return self.is_playing
    def Play(self,content:bytes):
        self.is_playing = True
        with wave.open(io.BytesIO(content),'rb') as f:
            width = f.getsampwidth()
            channels = f.getnchannels()
            rate = f.getframerate()
        pa = pyaudio.PyAudio()
        pa_stream = pa.open(
            format = pyaudio.get_format_from_width(width),
            channels = channels,
            rate=rate,
            output=True
        )
        pa_stream.write(content)
        sleep(0.5)
        self.is_playing = False