from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow,QApplication,QLabel,QPushButton
from PyQt5.QtWidgets import QToolTip,QLineEdit,QMenuBar,QAction
import sys
from PyQt5.QtCore import QDateTime,QCoreApplication

 
class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color:#7CB9E8;")
        self.datetime = QDateTime.currentDateTime().toString()
        self.setWindowTitle(self.datetime)
        self.setGeometry(100,200,680,540)

        message = "This is a window that'll take an input"
        self.label = QLabel(message,self)
        self.label.move(100,100)
        
        btn1 = QPushButton("Btn1",self)
        btn1.setToolTip("Btn1")
        btn1.move(350,250)
        btn1.clicked.connect(self.changeWindow)
        #import matplotlib.pyplot as plt

        mainMenu = self.menuBar()
        mainMenu.setStyleSheet("background-color:pink;")


        fileMenu = mainMenu.addMenu("File")
        editMenu = mainMenu.addMenu("Edit")

        exitButton = QAction("Exit",self)
        exitButton.setShortcut("Ctrl+Q")
        exitButton.triggered.connect(self.Close)

        fileMenu.addAction(exitButton)
        fileMenu.setStyleSheet("background-color:#00FFFF;")
        
        self.InitUI()

    def InitUI(self):

        self.lineEdit = QLineEdit(self)
        self.lineEdit.resize(300,30)
        self.lineEdit.move(200,200)
        self.lineEdit.setStyleSheet("background-color:lightblue;")

        btn1 = QPushButton("Process",self)
        btn1.setToolTip("Process the string")
        btn1.move(260,250)


        self.statusBar = self.statusBar()
        self.statusBar.setStyleSheet("background-color:pink;")
        self.show()
        
    def Close(self):
        QCoreApplication.instance().quit()
        

    def changeWindow(self):
        self.newWindow = SecondWindow()
        self.newWindow.show()
        

class SecondWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.datetime = QDateTime.currentDateTime().toString()
        self.setWindowTitle(self.datetime)
        self.setGeometry(100,200,680,540)
        self.label = QLabel("Window",self)
        self.label.move(100,200)
        
        self.lineEdit = QLineEdit(self)
        self.lineEdit.move(100,300)
        self.lineEdit.resize(200,100)
        
        btn1 = QPushButton("Save",self)
        btn1.setToolTip("Save it")
        btn1.move(230,500)
        


def main():
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
