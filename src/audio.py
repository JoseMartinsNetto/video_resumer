from pydub import AudioSegment
import librosa
import soundfile as sf

class Audio:
    def __init__(self, path: str):
        self.path = path

    def convert_to_wav(self) -> str:
        audio = AudioSegment.from_file(self.path)
        wav_file = self.path.replace('.mp4', '.wav')
        audio.export(wav_file, format="wav")
        return wav_file

    def convert_to_mono(self):
        y, sr = librosa.load(self.path, mono=False)
        y_mono = librosa.to_mono(y)
        sf.write(self.path, y_mono, sr)