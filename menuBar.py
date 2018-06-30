from PyQt5.QtCore import QDateTime
from PyQt5.QtWidgets import QApplication,QMainWindow,QPushButton,QAction,QStatusBar
import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication

class Window(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setGeometry(200,200,680,540)
        self.datetime = QDateTime.currentDateTime().toString()
        self.setStyleSheet("background-color:grey;")
        self.setWindowTitle("Pritam "+self.datetime)
        
        self.statusbar = self.statusBar()
        self.statusbar.setStyleSheet("background-color:lightblue;")

        btn1 = QPushButton("Click Me",self)
        btn1.move(200,200)
        btn1.setToolTip("Click it ")
        btn1.setStyleSheet("background-color : lightblue;")

        self.InitUI()

    def InitUI(self):

        mainMenu = self.menuBar()

        fileMenu = mainMenu.addMenu("File")
        viewMenu = mainMenu.addMenu("View")
        editMenu = mainMenu.addMenu("Edit")
        toolMenu = mainMenu.addMenu("Tools")
        helpMenu = mainMenu.addMenu("Help")

        exitButton = QAction(QIcon("logo.png"),"Exit",self)
        exitButton.setShortcut("Ctrl+E")
        exitButton.triggered.connect(self.close)
        fileMenu.addAction(exitButton)

        openButton = QAction(QIcon("logo.png"),"Open",self)
        openButton.setShortcut("Ctrl+O")
        openButton.triggered.connect(self.close)
        fileMenu.addAction(openButton)
        self.show()

    def close(self):
        QCoreApplication.instance().quit()


def main():
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
