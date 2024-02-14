# from PyQt6.QtWidgets import QApplication
from audio_to_text_parser import AudioToTextParser
from youtube_helper import YouTubeHelper

def onDownloadProgress(percentage):
    print(percentage)

def onParsingToTextProgress(percentage: float):
    print(percentage)

if __name__ == '__main__':
    url = 'https://www.youtube.com/watch?v=KOFTYu09Z6U&ab_channel=Li%C3%A7%C3%B5esdeValor'

    # downloader = YouTubeHelper(url, onProgress=onDownloadProgress)
    # audioPath = downloader.downloadWavAudio()

    audioPath = "/Users/josemartins/Downloads/WhatsApp-Ptt-2024-01-29-at-23.43.10.wav"

    audioParser = AudioToTextParser(audioPath, onProgress=onParsingToTextProgress)
    text = audioParser.parse()

    # app = QApplication(sys.argv)
    # gallery = AppUi()
    # gallery.show()
    # sys.exit(app.exec())
