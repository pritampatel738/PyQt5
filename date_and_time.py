import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5 import QtGui
from PyQt5.QtCore import QDateTime,QDate,QTime


class Window(QMainWindow):

    def __init__(self):

        super().__init__()
        self.time = QTime.currentTime().toString()
        self.date = QDate.currentDate().toString()
        self.datetime = QDateTime.currentDateTime().toString()
        self.InitWindow()


    def InitWindow(self):
        
        self.setWindowTitle(self.datetime)
        self.setGeometry(100,100,500,300)
        self.show()

def main():
    app = QApplication(sys.argv)
    window = Window()
    print("closed")
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
