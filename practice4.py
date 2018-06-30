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
        self.setGeometry(200,200,680,540)
        self.datetime = QDateTime.currentDateTime().toString()
        self.setWindowTitle(self.datetime)
        
        self.setWindowIcon(QIcon("logo.png"))

        menuBar = self.menuBar()
        menuBar.setStyleSheet("background-color:lightblue;")

        fileMenu = menuBar.addMenu("File")
        editMenu = menuBar.addMenu("Edit")
        viewMenu = menuBar.addMenu("View")
        toolMenu = menuBar.addMenu("Tool")
        helpMenu = menuBar.addMenu("Help")

        # adding toolbar ....
        copyAct = QAction(QIcon("logo.png"),"Copy",self)
        copyAct.setShortcut("Ctrl+C")

        pasteAct = QAction(QIcon("logo.png"),"Paste",self)
        pasteAct.setShortcut("Ctrl+V")

        
        self.toolbar = self.addToolBar("Toolbar")
        self.toolbar.addAction(copyAct)
        self.toolbar.addAction(pasteAct)
        


        # adding status bar ......
        self.statusbar = self.statusBar()
        self.statusbar.setStyleSheet("background-color:lightblue;")
        self.InitUI()

    def InitUI(self):



        self.show()


def main():
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
