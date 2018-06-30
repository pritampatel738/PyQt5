from PyQt5.QtCore import QDateTime
from PyQt5.QtWidgets import QApplication,QMainWindow,QPushButton,QAction,QStatusBar
import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QMenu


class Window(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setStyleSheet("background-color:lightblue;")
        self.setGeometry(200,200,680,540)
        self.datetime = QDateTime.currentDateTime().toString()

        self.setWindowTitle(self.datetime)

        btn1 = QPushButton("ABC",self)
        btn1.move(100,100)
        btn1.setStyleSheet("background-color:blue;")
        btn1.clicked.connect(self.Context_Menu)

        self.statusbar = self.statusBar()
        self.statusbar.setStyleSheet("background-color:grey;")

        mainMenu = self.menuBar()

        fileMenu = mainMenu.addMenu("File")
        editMenu = mainMenu.addMenu("Edit")
        viewMenu = mainMenu.addMenu("View")
        toolMenu = mainMenu.addMenu("Tools")
        helpMenu = mainMenu.addMenu("Help")


        new = QAction(QIcon("logo..png"),"New",self)
        new.setShortcut("Ctrl+N")
        fileMenu.addAction(new)
        



        self.InitUI()

    def InitUI(self):
        
        self.show()

    def Context_Menu(self,event):

        contextMenu = QMenu(self)
        newAct = QAction("New",self)
        openAct = QAction("Open",self)
        quitAct = QAction("Quit",self)

        action = contextMenu.exec_(self.mapToGlobal(event.pos()))

        if action == quitAct:
            QCoreApplication.instance().quit()

        elif action==newAct:
            print("New window is opened")
        elif action == openAct:
            print("Choose the existing file")
        


def main():
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
