from text_resumer import TextResumer
import utils
from whisper_audio_to_text_parser import WhisperAudioToTextParser

def on_download_progress(percentage: float):
    percentage = "{:.0f}".format(percentage)
    print('\033[H\033[J')
    print(f'Download: {percentage}%')

def on_parsing_progress(current_segments: list, processing_segment: int, left_segment: int, rate: float):
    print('\033[H\033[J')
    utils.print_header('Parsing to text')
    rate = "{:.2f}".format(rate * 100)
    print(f'{rate}%')

if __name__ == '__main__':
    try:
        audioPath = '/Users/josemartins/Projects/Jose/Python/video_resumer/downloads/Google perde disputa contra Epic Games O mundo dos apps irá mudar.wav'
        # url = 'https://www.youtube.com/watch?v=5AhCLOOQVx0'
        # downloader = YouTubeDownloader(url, onProgress=on_download_progress)
        # audioPath = downloader.download_wav_audio()

        # whisperParser = WhisperAudioToTextParser(audioPath)
        # whisper_result = whisperParser.parse(on_parsing_progress=on_parsing_progress)

        # utils.saveToFile(f'Whisper_Result.txt', whisper_result['text'])

        text = utils.readFromFile(f'Whisper_Result.txt')
        sumarizer = TextResumer(text)

        summary = sumarizer.resume()
        print(summary)

    except Exception as e:
        print(e)

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # whisperParser = WhisperAudioToTextParser(audioPath)
    # text = whisperParser.parse()

    # app = QApplication(sys.argv)
    # gallery = AppUi()
    # gallery.show()
    # sys.exit(app.exec())



# def onParsingToTextProgress(percentage: float, count: int):
#     percentage = "{:.0f}".format(percentage)
#     print('\033[H\033[J')
#     print(f'Parsing to text: {percentage} - count: {count}%')