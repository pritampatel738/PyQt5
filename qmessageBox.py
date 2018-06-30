import sys
from PyQt5.QtCore import QDate,QTime,QDateTime
from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5.QtWidgets import QMessageBox,QPushButton,QToolTip
from PyQt5 import QtGui
from PyQt5.QtCore import QCoreApplication


class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.datetime = QDateTime.currentDateTime().toString()
        self.setStyleSheet("background-color: grey;")
        
        btn1 = QPushButton("Close",self)
        btn1.move(100,100)
        btn1.setToolTip("Close the App")
        btn1.clicked.connect(self.CloseApp)
        btn1.setStyleSheet("background-color: red;")


        btn2 = QPushButton("Question",self)
        btn2.move(200,100)
        btn2.setToolTip("Get a Question")
        btn2.clicked.connect(self.Question)
        btn2.setStyleSheet("background-color: blue;")

        btn3 = QPushButton("About",self)
        btn3.move(300,100)
        btn3.setToolTip("About Me")
        btn3.clicked.connect(self.About)
        btn3.setStyleSheet("background-color: green;")
        
        self.InitUI()

        
    def InitUI(self):
        self.setGeometry(200,200,600,400)
        self.setWindowTitle("Pritam "+str(self.datetime))

        self.show()

    def CloseApp(self):
        title = "Closing the App"
        Message = "Are you sure you want to close the app?"
        
        reply = QMessageBox.question(self,title,Message,QMessageBox.Yes | QMessageBox.No,QMessageBox.No)
        if reply == QMessageBox.Yes:
            QCoreApplication.instance().quit()


            

    def Question(self):
        message = QMessageBox.question(self,"Question","Close?",QMessageBox.Yes | QMessageBox.No,QMessageBox.No)
        if message == QMessageBox.No:
            QCoreApplication.instance().quit()

    def About(self):
        message_to_be_displayed = "This page is a simple page ."
        title = "About the page"
        message = QMessageBox.about(self,title,message_to_be_displayed)
        

def main():
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
