import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget,     QPushButton, QHBoxLayout
import objects

app = QApplication([])
#window = QWidget()
#window.setWindowTitle("Sovl Music player")
#layout = QHBoxLayout()
#
#pluy=objects.MediaButton(0,0,0,0,"test","play_pause")
#play=QPushButton("play/pause")
#
#
#layout.addWidget(play)
#
#layout.addWidget(QPushButton("Center"))
#
#layout.addWidget(QPushButton("Right"))
#
#window.setLayout(layout)
##helloMsg = QLabel("<h1>Hello, World!</h1>", parent=window)
##helloMsg.move(60, 15)
window=objects.window()
layout=QHBoxLayout()
layout.addWidget(objects.MediaButton())
layout.addWidget(objects.MediaButton())
layout.addWidget(objects.MediaButton())
layout.addWidget(objects.MediaButton())
layout.addWidget(objects.MediaButton())
window.setLayout(layout)
window.show()

sys.exit(app.exec())
