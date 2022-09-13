
import funcs
from PyQt5.QtWidgets import  QWidget, QPushButton
from PyQt5.QtGui import QIcon,QPixmap,QPainter
from PyQt5.QtCore import pyqtSlot, Qt, QPoint, QSize

class MediaButton(QPushButton):
    def __init__(self):
       super().__init__()
       x=0
       y=0
       height=10
       width=10
       shape=0
       img="test.jpg"
       self.func= "play_pause"
       self.setGeometry(x,y,height,width)
       self.setIcon(QIcon(img))
       self.clicked.connect(self.on_click)

    @pyqtSlot()
    def on_click(self):
        self.run(self.func) 

    def run(self,func):
        match func:
            case "play_pause":
                funcs.play_pause()
            case "random":
                funcs.random()
            case "shuffle":
                funcs.shuffle()
            case "stop":
                funcs.stop()
            case "prev":
                funcs.prev()
            case "next":
                funcs.next()

class window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sovl Music player")
        self.setWindowIcon(QIcon("test.jpg"))
        self.setGeometry(100, 100, 280, 80)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
    def sizeHint(self):
        return QSize(720, 720) # Set this to the exact image resolution

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)    
        pixmap = QPixmap()
        pixmap.load('fondotest.png')
        qp.drawPixmap(QPoint(0, 0), pixmap)    
        qp.end()

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()
