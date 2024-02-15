
from PyQt6.QtWidgets import ( QDialog, QGridLayout,  QHBoxLayout, QLabel, QLineEdit, QPushButton)

class AppUi(QDialog):

    def __init__(self, parent=None):
        super(AppUi, self).__init__(parent)
        self.setFixedWidth(500)
        self.setFixedHeight(500)
        
        textField = QLineEdit()
        videoLabel = QLabel("&Url do vídeo:")
        videoLabel.setBuddy(textField)

        searchButton = QPushButton("Processar")
        searchButton.clicked_connect()

        topLayout = QHBoxLayout()
        topLayout.addWidget(videoLabel)
        topLayout.addWidget(textField)
        topLayout.addWidget(searchButton)

        mainLayout = QGridLayout()
        mainLayout.addLayout(topLayout, 0, 0 ,0, 0)

        self.setLayout(mainLayout)
        self.setWindowTitle("Video Resumer")

# from PyQt6.QtCore import QDateTime, Qt, QTimer
# QApplication, QCheckBox, QComboBox, QDateTimeEdit,
#         QDial, QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
#         QProgressBar, QPushButton, QRadioButton, QScrollBar, QSizePolicy,
#         QSlider, QSpinBox, QStyleFactory, QTableWidget, QTabWidget, QTextEdit,
#         QVBoxLayout, QWidget