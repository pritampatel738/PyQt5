from PyQt5.QtWidgets import QPushButton,QApplication,QLabel,QLineEdit
import sys
from PyQt5.QtCore import QDateTime
from PyQt5.QtWidgets import QMainWindow,QDialog,QMenuBar,QAction,QStatusBar




class Window(QDialog):

    def __init__(self):
        super().__init__()
        self.InitUI()


    def InitUI(self):
        self.setGeometry1()
        self.makeMenuBar()
        self.setButtons()
        self.colorManagement()

        self.show()
        
    def setGeometry1(self):
        self.dateTime = QDateTime.currentDateTime().toString()
        self.setWindowTitle(self.dateTime)
        
        self.setGeometry(100,100,680,540)

    def makeMenuBar(self):
        self.statusBar = QStatusBar()
        
        self.mainMenu = QMenuBar()
        
        self.fileMenu = self.mainMenu.addMenu("File")
        self.editMenu = self.mainMenu.addMenu("Edit")

        self.newWindow = QAction("New",self)
        self.find = QAction("Find",self)

        self.fileMenu.addAction(self.newWindow)
        self.fileMenu.addAction(self.find)
        
        self.editMenu.addAction(self.find)
        self.editMenu.addAction(self.newWindow)

        

    def setButtons(self):
        self.btn1 = QPushButton("Process",self)
        self.btn1.move(100,100)

    def colorManagement(self):
        self.setStyleSheet("background-color:grey;")
        self.btn1.setStyleSheet("background-color:#7CB9E8;")
        self.mainMenu.setStyleSheet("background-color:#54626F;")
        self.statusBar.setStyleSheet("background-color:#54626F;")
        pass


def main():
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
