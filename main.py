import sys
from PyQt5.QtWidgets import QApplication, QWidget

class OCRViewer(QWidget):
    def __init__(self):
        super().__init__()
        self.init_UI()

    def init_UI(self):
        """
        Initialize the graphic interface
        """
        self.resize(300, 300)
        self.setWindowTitle('OCR Viewer')

        self.show()
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ocrviewer = OCRViewer()
    sys.exit(app.exec_())
