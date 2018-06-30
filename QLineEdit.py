from PyQt5.QtCore import QDateTime
from PyQt5.QtWidgets import QLineEdit,QApplication,QMessageBox,QMainWindow,QPushButton,QAction,QStatusBar
import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QMenu
from PyQt5 import QtGui


class Window(QMainWindow):

    def __init__(self):
        
        super().__init__()
        self.setGeometry(100,100,680,540)
        self.datetime = QDateTime.currentDateTime().toString()
        self.setWindowTitle("Pritam "+self.datetime)

        self.statusbar = self.statusBar()
        self.statusbar.setStyleSheet("background-color:lightblue;")

        

        mainMenu = self.menuBar()
        mainMenu.setStyleSheet("background-color:lightblue;")

        fileMenu = mainMenu.addMenu("File")
        editMenu = mainMenu.addMenu("Edit")
        viewMenu = mainMenu.addMenu("View")
        toolMenu = mainMenu.addMenu("Tools")
        helpMenu = mainMenu.addMenu("Help")

        newAct = QAction(QIcon("logo.png"),"New",self)
        newAct.setShortcut("Ctrl+N")
        fileMenu.addAction(newAct)
        
        self.setWindowIcon(QtGui.QIcon("logo.png"))
        self.InitWindow()

    def InitWindow(self):
        
        exitAct = QAction(QIcon("logo.png"),"Exit",self)
        exitAct.setShortcut("Ctrl+E")

        copyAct = QAction("Copy",self)
        copyAct.setShortcut("Ctrl+C")

        pasteAct = QAction(QIcon("logo.png"),"Paste",self)
        pasteAct.setShortcut("Ctrl+V")

        self.toolbar = self.addToolBar("Toolbar")
        self.toolbar.addAction(exitAct)
        self.toolbar.addAction(copyAct)
        self.toolbar.addAction(pasteAct)

        self.lineedit = QLineEdit(self)
        self.lineedit.move(200,200)
        self.lineedit.resize(300,30)

        btn1 = QPushButton("Submit",self)
        btn1.move(280,235)
        btn1.resize(100,25)
        btn1.clicked.connect(self.submitClicked)
        
        
        self.show()

    def submitClicked(self):
        text = self.lineedit.text()
        title = "Typed text"
        QMessageBox.about(self,title,text)



        

def main():
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
    
