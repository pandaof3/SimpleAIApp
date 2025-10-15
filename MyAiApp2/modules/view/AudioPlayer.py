import pyaudio
import wave
import io
from modules.interfaces.AudioPlayer import IAudioPlayer
class AudioPlayer(IAudioPlayer):
    def Play(self,content:bytes):
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