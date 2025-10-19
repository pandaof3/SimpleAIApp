import pyaudio
import wave
import io
from time import sleep
from modules.interfaces.AudioPlayer import IAudioPlayer
class AudioPlayer(IAudioPlayer):

    is_playing = False
    stream = None
    def Playing(self) -> bool:
        return self.is_playing
    def Play(self,content:bytes):
        self.is_playing = True
        with wave.open(io.BytesIO(content),'rb') as f:
            width = f.getsampwidth()
            channels = f.getnchannels()
            rate = f.getframerate()
            audio_data = f.readframes(f.getnframes())
        pa = pyaudio.PyAudio()
        pa_stream = pa.open(
                format = pyaudio.get_format_from_width(width),
                channels = channels,
                rate=rate,
                output=True
            )
        pa_stream.write(audio_data)
        pa.terminate()
        '''
        with wave.open("test.wav",'wb') as f:
            f.setnchannels(channels)
            f.setsampwidth(width)
            f.setframerate(rate)
            f.writeframes(audio_data)
            print("audio saved as test.wav")
        '''
        self.is_playing = False