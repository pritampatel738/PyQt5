from PyQt5.QtCore import QDateTime
from PyQt5.QtWidgets import QApplication,QMainWindow,QPushButton,QAction,QStatusBar
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
        self.setStyleSheet("background-color:lightblue;")

        self.statusbar = self.statusBar()
        self.statusbar.setStyleSheet("background-color:blue;")

        btn1 = QPushButton("Button",self)
        btn1.move(0,100)
        btn1.setToolTip("Button")
        btn1.setShortcut("Ctrl+B")

        mainMenu = self.menuBar()

        fileMenu = mainMenu.addMenu("File")
        editMenu = mainMenu.addMenu("Edit")
        viewMenu = mainMenu.addMenu("View")
        toolMenu = mainMenu.addMenu("Tools")
        helpMenu = mainMenu.addMenu("Help")

        newAct = QAction(QIcon("logo.png"),"New",self)
        newAct.setShortcut("Ctrl+N")
        fileMenu.addAction(newAct)

        findAct = QAction(QIcon("logo.png"),"Find",self)
        findAct.setShortcut("Ctrl+F")
        editMenu.addAction(findAct)
        
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

        
        
        self.show()

def main():
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
    
