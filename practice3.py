import sys
from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5.QtWidgets import QPushButton,QToolTip,QMessageBox
from PyQt5.QtCore import QDateTime,QCoreApplication
from PyQt5 import QtGui

class Window(QMainWindow):

    def __init__(self):

        super().__init__()
        self.setGeometry(200,200,600,500)
        self.datetime = QDateTime.currentDateTime().toString()
        
        self.setWindowTitle("Pritam  "+self.datetime)
        self.setWindowIcon(QtGui.QIcon("logo.png"))

        self.setStyleSheet("background-color: black;")
        
        btn1 = QPushButton("Close",self)
        btn1.move(300,300)
        btn1.resize(70,20)
        btn1.setStyleSheet("background-color:grey;")
        btn1.clicked.connect(self.Close)
        btn1.setToolTip("Close")
        

        self.show()

    def Close(self):
        self.setStyleSheet("background-color:white;")
        title = "Closing"
        msg = "Are you sure you want to close this app"
        message = QMessageBox.question(self,title,msg,QMessageBox.Yes | QMessageBox.No,QMessageBox.No)
        if message == QMessageBox.Yes:
            QCoreApplication.instance().quit()


def main():
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
