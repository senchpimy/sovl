import funcs
from threading import Thread
import logging
from PyQt5.QtWidgets import  QMainWindow, QSlider
from PyQt5.QtGui import QIcon,QPixmap,QPainter
from PyQt5.QtCore import  Qt, QPoint
import time
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

       elif func=="repeat":
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
        pixmap.load(self.Image)
        qp.drawPixmap(QPoint(0, 0), pixmap)    
        qp.end()

    def WindowConfig(self,config):
        image=config["Image"]
        self.setWindowIcon(QIcon(icon))
        self.setGeometry(config["X"], config["Y"], config["Height"],config["Width"])
        if image.endswith(".png"):
            self.setAttribute(Qt.WA_TranslucentBackground)
            self.Image=image
            return False,""
        else:
            return True,image

def a(slider):
    while True:
        slider.setValue(funcs.get_progress())
        time.sleep(1)

def Slider(slider,config):
    slider.setGeometry(config["x"], config["y"], config["height"],config["width"])
    slider.setMinimum(0)
    slider.setMaximum(100)

    if config["func"]=="vol":
        slider.setTickInterval(50)
        slider.setValue(funcs.get_vol())
        slider.valueChanged[int].connect(funcs.set_volume)

    elif config["func"]=="progress":
        slider.setTickInterval(100)
        slider.sliderReleased.connect(lambda: funcs.song_seek(slider.value()))
        slider.setValue(funcs.get_progress())
        ab=Thread(target=a,args=(slider,))
        ab.start()
