#!/usr/bin/env python3
import sys
sys.path.insert(1, '/home/plof/Documents/PythonProjects/sovl/souvl_lib')
from PyQt5.QtWidgets import QApplication, QPushButton, QSlider
app = QApplication([])
import objects
import config

window=objects.window()
windowconfig, buttonsConfig, slider=config.read_config("/home/plof/.config/sovl/config.ini")
windowconfig["Image"]=config.image_config(windowconfig)
background,string=window.WindowConfig(windowconfig)

if background :
    stylesheet = f"""
    window {{
        background-image: url("{string}"); 
        background-repeat: no-repeat; 
        background-position: center;
    }}
"""
    app.setStyleSheet(stylesheet)

for i in buttonsConfig:
    objects.MediaButton(QPushButton(window),i["x"],i["y"],i["height"],i["width"],i["image"],i["func"],i["shape"])
#    print(i["x"],i["y"],i["height"],i["width"],i["Image"],i["func"],i["shape"])
#    print(type(i["x"]),type(i["y"]),type(i["height"]),type(i["width"]),type(i["Image"]),type(i["func"]),type(i["shape"]))
if slider:
    slider=objects.Slider(QSlider(window))
    slider.setGeometry(30, 40, 200, 30)

window.show()
sys.exit(app.exec())

