from PyQt5 import QtGui
import sys
from PyQt5.QtWidgets import QApplication,QMainWindow

class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.InitWindow()

    def InitWindow(self):

        self.setGeometry(100,100,500,300)
        self.setWindowIcon(QtGui.QIcon("logo.png"))
        self.setWindowTitle("Pritam")

        self.show()

def main():
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
