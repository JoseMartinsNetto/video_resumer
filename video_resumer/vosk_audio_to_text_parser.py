
import os
import time
from typing import Callable, Optional
from vosk import Model, KaldiRecognizer
import wave
import json
import librosa
import soundfile as sf
from typing import List
from concurrent.futures import ThreadPoolExecutor, Future

from audio import Audio

class VoskAudioToTextParser:
    def __init__(self,
                 path: str,
                 modelName: str,
                 onProgress: Optional[Callable[[float, int], None]] = None,
                 onInit: Optional[Callable[[dict], None]] = None,
                 onExecute: Optional[Callable[[str, str], None]] = None,
                 ) -> None:
        self.path = path
        self.onProgress = onProgress
        self.modelName = modelName
        self.onInit = onInit
        self.onExecute = onExecute

    def __parse_audio_chunk(self, audioData: bytes, index: int, results: list):
        model = self.__initialize_model()
        rec = KaldiRecognizer(model, 16000)
        rec.SetWords(True)

        amountOfChunks = len(results)

        # self.onExecute(f"Chunk - {index} of {amountOfChunks}" , 'Processing...')

        if rec.AcceptWaveform(audioData):
            pass
            # self.onExecute(f"Chunk - {index} of {amountOfChunks}",'Ok.')

        results[index] = rec.Result()

    def __split_audio(self, estimatedChunks: int ):
        audioChunks = []

        with wave.open(self.path, "rb") as wf:
            totalFrames = wf.getnframes()

            chunkSize = int(totalFrames / estimatedChunks)

            if chunkSize >= totalFrames:
                return [wf.readframes(totalFrames)]

            currentFrame = 0
            while currentFrame < totalFrames:
                endFrame = min(currentFrame + chunkSize, totalFrames)
                chunkFrames = endFrame - currentFrame

                wf.setpos(currentFrame)
                audioChunks.append(wf.readframes(chunkFrames))

                currentFrame += chunkFrames

        return audioChunks
        
    def __initialize_model(self):
        workdir = os.getcwd()
        modelPath = f"{workdir}/resources/models/{self.modelName}"

        if not os.path.exists(modelPath):
            print("Por favor, baixe o modelo de linguagem do site do Vosk e extraia-o na pasta 'vosk-model-small-pt-0.3'")

        # Carregar o modelo de linguagem
        model = Model(modelPath, model_name=self.modelName, lang="pt-br")
        return model
    
    def parse(self, multithreanding: bool = False) -> str:
        if multithreanding:
            logs = {}
            audioChunks = self.__split_audio(estimatedChunks=12)
            amountOfChunks = len(audioChunks)
            results = [None] * amountOfChunks

            for i in range(amountOfChunks):
                logs[f"Chunk - {i} of {amountOfChunks}"] = 'Started'

            # self.onInit(logs)
            time.sleep(2)
            
            with ThreadPoolExecutor(max_workers=amountOfChunks) as executor:
                futures: List[Future] = []
                for i, chunk_data in enumerate(audioChunks):
                    futures.append(executor.submit(self.__parse_audio_chunk, chunk_data, i, results))

                for future in futures:
                    future.result()
                    print('future.result()')


            jsonResults = [json.loads(result) for result in results if result is not None]
            texts = [result['text'] for result in jsonResults if result is not None]

            combined_result = ';\n'.join(texts)
            return combined_result
        else:
            wf = wave.open(self.path, 'rb')

            if wf.getnchannels() != 1:
                Audio(self.path).convert_to_mono()
                wf = wave.open(self.path)

            model = self.__initialize_model()
            rec = KaldiRecognizer(model, wf.getframerate())

            while True:
                data = wf.readframes(4000)
                if len(data) == 0:
                    break
                rec.AcceptWaveform(data)

            res = json.loads(rec.FinalResult())
            return res['text']
