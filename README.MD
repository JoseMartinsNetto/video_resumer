# Resumir vídeos

## Requisitos

[ ] - Baixar videos ( YouTube, Google Drive );

[ ] - Extrair o audio e converter para texto;

[ ] - Criar o resumo do texto

Libs ( pytube, pyinstaller,  pydub) 


```python
import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import QMainWindow, QApplication

class VideoPlayer(QMainWindow):
    def _init_(self, video_path, parent=None):
        super(VideoPlayer, self)._init_(parent)
        self.setWindowTitle("Video Player")
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.videoWidget = QVideoWidget()
        self.setCentralWidget(self.videoWidget)
        self.mediaPlayer.setVideoOutput(self.videoWidget)
        self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(video_path)))
        self.mediaPlayer.play()

if _name_ == '_main_':
    app = QApplication(sys.argv)
    player = VideoPlayer('path_to_your_video.mp4')  
    player.show()
    sys.exit(app.exec_())
```