import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QHBoxLayout
app = QApplication([])
import objects
import config
import funcs

window=objects.window()
button1 = QPushButton(window)
objects.MediaButton(button1)
#layout=QHBoxLayout()
#window.addWidget(objects.MediaButton(10,20,35,40,objects.NextButton()))
#window.setLayout(layout)
window.show()

sys.exit(app.exec())


