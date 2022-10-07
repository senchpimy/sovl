#!/usr/bin/env python3
import sys, getopt
sys.path.insert(1, '/home/plof/Documents/PythonProjects/sovl/souvl_lib')
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QHBoxLayout
app = QApplication([])
import objects
import config
import funcs
import os

window=objects.window()
button1 = QPushButton(window)
usrconfig,buttons=config.read_config("/home/plof/.config/sovl/config.ini")
usrconfig["Image"]=config.image_config(usrconfig)
for i in usrconfig:
    print(i)
#layout=QHBoxLayout()
#window.addWidget(objects.MediaButton(10,20,35,40,objects.NextButton()))
#window.setLayout(layout)
window.show()
  
  
# Print the process ID of
# the current process
sys.exit(app.exec())


