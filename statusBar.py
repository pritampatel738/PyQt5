from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication,QMainWindow,QPushButton,QStatusBar
from PyQt5.QtCore import QDateTime
import sys



class Window(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setGeometry(100,100,680,540)
        self.datetime = QDateTime.currentDateTime().toString()
        
        self.setWindowTitle("Pritam "+self.datetime)
        

        self.InitUI()

    def InitUI(self):
        
        self.setStyleSheet("background-color:grey;")
        self.statusbar = self.statusBar()
        self.statusbar.showMessage("Status Bar")
        self.statusbar.setStyleSheet("background-color:blue;")
        
        self.show()


def main():
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())

if __name__=="__main__":
    main()
