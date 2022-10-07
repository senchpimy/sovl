#!/usr/bin/env python3
import sys
sys.path.insert(1, '/home/plof/Documents/PythonProjects/sovl/souvl_lib')
from PyQt5.QtWidgets import QApplication, QPushButton
app = QApplication([])
import objects
import config

window=objects.window()
button1 = QPushButton(window)
usrconfig,buttons=config.read_config("/home/plof/.config/sovl/config.ini")
usrconfig["Image"]=config.image_config(usrconfig)
background,string=window.WindowConfig(usrconfig)

if background :
    stylesheet = f"""
    window {{
        background-image: url("{string}"); 
        background-repeat: no-repeat; 
        background-position: center;
    }}
"""
    app.setStyleSheet(stylesheet)

window.show()
  
sys.exit(app.exec())
