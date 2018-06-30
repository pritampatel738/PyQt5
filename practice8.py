import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QLabel
from PyQt5.QtWidgets import QPushButton



class Window(QMainWindow):

    def __init__(self):

        super(Window,self).__init__()
        
        self.setGeometry(100,100,680,540)
        
        self.label1 = QLabel("Window1",self)
        self.label1.move(100,100)

        self.btn1 = QPushButton("New Window",self)
        self.btn1.move(100,150)
        self.style = """
                QPushButton{
                    background-color:grey;
                }
                QPushButton:hover {
                    background-color : blue;
                    color: grey;
                }

                Window{
                    background-color : black;
                }

                QLabel{
                    color : grey;
                }
            """
        self.setStyleSheet(self.style)
        self.btn1.clicked.connect(self.newWindow)

        self.show()
        
    def newWindow(Window):
        pass
        
        



def main():

    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
