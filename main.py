import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget,     QPushButton, QHBoxLayout
app = QApplication([])
import objects

window=objects.window()
layout=QHBoxLayout()
layout.addWidget(objects.MediaButton(10,20,35,40,objects.NextButton()))
layout.addWidget(objects.MediaButton())
window.setLayout(layout)
window.show()

sys.exit(app.exec())
