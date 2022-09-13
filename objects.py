
import funcs
from PyQt5.QtWidgets import  QWidget, QPushButton
from PyQt5.QtGui import QIcon,QPixmap,QPainter
from PyQt5.QtCore import pyqtSlot, Qt, QPoint, QSize



class PlayButton(QPushButton):
    def __init__(self):
       super().__init__()
       self.clicked.connect(self.on_click)

    @pyqtSlot()
    def on_click(self):
        funcs.play_pause()

class RandomButton(QPushButton):
    def __init__(self):
       super().__init__()
       self.clicked.connect(self.on_click)

    @pyqtSlot()
    def on_click(self):
        funcs.random()

class StopButton(QPushButton):
    def __init__(self):
       super().__init__()
       self.clicked.connect(self.on_click)

    @pyqtSlot()
    def on_click(self):
        funcs.stop()

class NextButton(QPushButton):
    def __init__(self):
       super().__init__()
       self.clicked.connect(self.on_click)

    @pyqtSlot()
    def on_click(self):
        funcs.next()

class PrevButton(QPushButton):
    def __init__(self):
       super().__init__()
       self.clicked.connect(self.on_click)

    @pyqtSlot()
    def on_click(self):
        funcs.prev()

class shuffleButton(QPushButton):
    def __init__(self):
       super().__init__()
       self.clicked.connect(self.on_click)

    @pyqtSlot()
    def on_click(self):
        funcs.shuffle()

def MediaButton(x=0,y=0,height=0,width=0,btn=PlayButton(),img="test.jpg"):
       btn.setGeometry(x,y,height,width)
       btn.setIcon(QIcon(img))
       btn.setStyleSheet("background-image : url({});".format(img))
       return btn

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
