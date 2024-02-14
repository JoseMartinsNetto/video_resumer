from typing import Any, Callable, Optional
from pytube import YouTube
from audio import Audio
import utils
import os

class YouTubeDownloader:
        def __init__(self,
                     url: str,
                     onProgress: Optional[Callable[[Any], None]] = None
            ) -> None:
             self.on_progress = onProgress
             self.url = url
             self.workdir = os.getcwd()

        def set_on_progress(self, func: Callable[[Any], None]) -> None:
              self.on_progress = func 

        def on_progress_callback(self, stream, chunks: bytes, bytes_remaining: int):
            total_size = stream.filesize
            bytes_downloaded = total_size - bytes_remaining
            percentage_of_completion = bytes_downloaded / total_size * 100
            self.on_progress(percentage_of_completion)

        def download(self, audioOnly: bool = False) -> str:
            yt = YouTube(self.url)
            yt.register_on_progress_callback(self.on_progress_callback)

            output_path = f'{self.workdir}/downloads'

            if(audioOnly):            
                return yt.streams.filter(only_audio=True).first().download(output_path=output_path)
            
            return yt.streams.order_by('resolution').first().download(output_path=output_path)
        
        def download_wav_audio(self) -> str:
            path = self.download(audioOnly=True)
            wav_file = Audio(path).convert_to_wav()

            utils.delete_file(path)
            return wav_file
             
