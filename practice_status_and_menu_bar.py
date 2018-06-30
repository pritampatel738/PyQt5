from PyQt5.QtWidgets import QPushButton,QApplication,QLabel,QLineEdit
import sys
from PyQt5.QtCore import QDateTime
from PyQt5.QtWidgets import QMainWindow,QDialog,QMenuBar,QAction,QStatusBar


class Window(QMainWindow,QDialog):
    def __init__(self):
        super().__init__()

        self.mainMenu = self.menuBar()
        self.fileMenu = self.mainMenu.addMenu("FIle")

        self.statusBar = QStatusBar()
        self.show()


app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec())
