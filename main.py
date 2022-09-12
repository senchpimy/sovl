import sys
import funcs
from PyQt6.QtWidgets import QApplication, QLabel, QWidget,     QPushButton, QHBoxLayout

class MediaButton(object):
    def __init__(self, x, y,height, width, shape,func):
       self.x=0
       self.y=0
       self.height=10
       self.width=10
       self.shape=0
       self.func= "play_pause"

    def run(self):
        match self.func:
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



app = QApplication([])
window = QWidget()
window.setWindowTitle("Sovl Music player")
window.setGeometry(100, 100, 280, 80)
layout = QHBoxLayout()
play=QPushButton("play/pause")


layout.addWidget(play)

layout.addWidget(QPushButton("Center"))

layout.addWidget(QPushButton("Right"))

window.setLayout(layout)
#helloMsg = QLabel("<h1>Hello, World!</h1>", parent=window)
#helloMsg.move(60, 15)
window.show()

sys.exit(app.exec())
