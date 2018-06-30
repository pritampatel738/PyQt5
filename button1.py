import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QMessageBox,QPushButton
from PyQt5.QtWidgets import QToolTip
from PyQt5.QtCore import QDate,QDateTime,QTime
from PyQt5.QtCore import QCoreApplication



from PyQt5 import QtGui


class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        
        self.setGeometry(200,200,680,540)
        self.datetime = QDateTime.currentDateTime().toString()

        button1 = QPushButton("Close",self)
        button1.move(100,100)
        button1.setToolTip("Close App")
        button1.clicked.connect(self.CloseApp)

        button2 = QPushButton("New Window",self)
        button2.move(200,100)
        button2.setToolTip("Click here for new window")
        button2.clicked.connect(self.NewWindow)
        
        self.InitUi()

        

    def InitUi(self):
        self.setWindowTitle("Pritam "+str(self.datetime))
        self.show()

    def CloseApp(self):
        QCoreApplication.instance().quit()

    def NewWindow(self):
        main()


    

def main():
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
