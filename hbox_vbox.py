import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QPushButton,QDialog
from PyQt5.QtWidgets import QMenuBar,QAction,QStatusBar,QLabel,QLineEdit
from PyQt5.QtCore import QDateTime
from PyQt5.QtWidgets import QHBoxLayout,QVBoxLayout,QGroupBox,QLabel,QGridLayout


class Window(QDialog):

    def __init__(self):
        super().__init__()
        self.dateTime = QDateTime.currentDateTime().toString()

        self.setWindowTitle(self.dateTime)
        self.setGeometry(100,100,680,540)

        self.InitUI()

    def InitUI(self):
        self.makeMenu()
        self.setButton()
        self.LineEdit()
        self.colorManagement()
        self.setLabel()
        self.horizontalLayout()
        self.verticalLayout()



        
        self.show()
        pass

    def horizontalLayout(self):
        self.groupBox = QGroupBox("GroupBox")

        hBoxLayout = QVBoxLayout()
        hBoxLayout.addWidget(self.btn1)
        hBoxLayout.addWidget(self.btn2)
        hBoxLayout.addWidget(self.btn3)
        hBoxLayout.addWidget(self.lineEdit)
        hBoxLayout.addWidget(self.label1)
        hBoxLayout.addWidget(self.customButton)
        hBoxLayout.addWidget(self.mainMenu)

        self.groupBox.setLayout(hBoxLayout)

        
    def verticalLayout(self):
        vBoxLayout = QHBoxLayout()
        vBoxLayout.addWidget(self.groupBox)
        self.setLayout(vBoxLayout)

        pass
    

    def setLabel(self):

        self.label1 = QLabel("Single Window : ",self)
        self.label1.move(10,50)

        pass

    def makeMenu(self):
        self.statusBar = QStatusBar()
        self.mainMenu = QMenuBar()
        
        self.fileMenu = self.mainMenu.addMenu("File")
        self.editMenu = self.mainMenu.addMenu("Edit")
        self.helpMenu = self.mainMenu.addMenu("Help")

        self.newWindow = QAction("New",self)
        self.newWindow.setShortcut("Ctrl+N")

        self.find = QAction("Find",self)
        self.find.setShortcut("Ctrl+F")

        self.help = QAction("Help",self)
        self.help.setShortcut("Ctrl+H")

        
        self.fileMenu.addAction(self.newWindow)
        self.editMenu.addAction(self.find)
        self.helpMenu.addAction(self.help)

        pass

    def setButton(self):
        self.btn1 = QPushButton("Button1",self)
        #self.btn1.move(100,100)
        self.btn1.setStatusTip("Button1")

        self.btn2 = QPushButton("Button2",self)
        #self.btn2.move(210,100)
        self.btn2.setStatusTip("Button2")

        self.btn3 = QPushButton("Button3",self)
        #self.btn3.move(320,100)
        self.btn3.setStatusTip("Button3")

        self.customButton = QPushButton("Custom",self)
        #self.customButton.move(100,1000)

        
    def LineEdit(self):
        self.lineEdit = QLineEdit(self)
        #self.lineEdit.move(130,50)
        self.lineEdit.resize(300,30)
        pass

    def colorManagement(self):
        self.setStyleSheet("background-color:lightblue;")
        
        self.btn1.setStyleSheet("background-color:pink;")
        self.btn2.setStyleSheet("background-color:lightgreen;")
        self.btn3.setStyleSheet("background-color:lightgrey;")

        self.mainMenu.setStyleSheet("background-color:pink;")
        
        self.fileMenu.setStyleSheet("background-color:violet;")
        self.editMenu.setStyleSheet("background-color:lightgrey;")
        self.helpMenu.setStyleSheet("background-color:lightgreen;")
        self.statusBar.setStyleSheet("background-color:pink;")

        self.lineEdit.setStyleSheet("background-color:lightgrey;")


def main():
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())


if __name__=="__main__":
    main()
