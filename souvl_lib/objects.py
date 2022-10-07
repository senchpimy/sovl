import funcs
import logging
from PyQt5.QtWidgets import  QWidget, QPushButton, QMainWindow
from PyQt5.QtGui import QIcon,QPixmap,QPainter
from PyQt5.QtCore import  Qt, QPoint, QSize
icon="/usr/bin/sovl/icon.jpg"

def MediaButton(btn,x=10,y=10,height=10,width=10,img="test.jpg",func="play_pause",shape="Default"):
       btn.setGeometry(x,y,height,width)
       btn.setIcon(QIcon(img))
       if shape=="Default":
           btn.setStyleSheet(f"background-image : url({img});")
       elif shape=="Circle":
           btn.setStyleSheet(f"background-image : url({img});border-radius : {int(x/2)}; ")

       if func=="play_pause":
            btn.clicked.connect(funcs.play_pause)

       elif func=="shuffle":
           btn.clicked.connect(funcs.shuffle)

       elif func=="prev":
           btn.clicked.connect(funcs.prev)

       elif func=="next":
           btn.clicked.connect(funcs.next)

       elif func=="stop":
           btn.clicked.connect(funcs.shuffle)

       elif func=="random":
           btn.clicked.connect(funcs.random)

       else:
           logging.error("function for the button not suported or invalid")

class window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sovl Music player")
        self.setWindowFlags(Qt.FramelessWindowHint)

    def paintEvent(self,event ):
        qp = QPainter()
        qp.begin(self)    
        pixmap = QPixmap()
        pixmap.load('fondotest.png')
        qp.drawPixmap(QPoint(0, 0), pixmap)    
        qp.end()


    def WindowConfig(self,config):
        image=config["Image"]
        self.setWindowIcon(QIcon(icon))
        self.setGeometry(config["X"], config["Y"], config["Height"],config["Width"])
        if image.endswith(".png"):
            self.setAttribute(Qt.WA_TranslucentBackground)
            qp = QPainter()
            qp.begin(self)    
            pixmap = QPixmap()
            pixmap.load(image)
            qp.drawPixmap(QPoint(0, 0), pixmap)    
            qp.end()
            return False,""
        else:
#            string=f"background-image : url('{image}');"
            return True,image
