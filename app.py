from PySide6.QtWidgets import QApplication, QMainWindow
from ui_speech_timer import Ui_MainWindow

class SpeechTimerApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

app = QApplication([])
window = SpeechTimerApp()
window.show()
app.exec()