import sys
from PyQt5 import QtGui
from PyQt5.QtCore import QDateTime,QDate,QTime
from PyQt5.QtWidgets import QMainWindow,QApplication,QLabel


class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        # setting the value of date and time ....
        self.datetime = QDateTime.currentDateTime().toString()

        # setting the value of time .......
        self.time = QTime.currentTime().toString()
        self.time1 = self.time[:6]
        
        # setting the value of date ......
        self.date = QDate.currentDate().toString()
        self.date1 = self.date[:5]

        # setting the title of window .....
        self.setWindowIcon(QtGui.QIcon("logo.png"))
        self.InitWindow()
        
    def InitWindow(self):
        # setting the value of margin on top , left
        # width and height ......
        self.setGeometry(300,200,530,300)
        
        # set the title of the window .......
        self.setWindowTitle("Pritam "+str(self.datetime))
        self.show()

    


def main():
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())
    

if __name__ == "__main__":
    main()








