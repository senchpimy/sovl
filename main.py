#!/usr/bin/env python3
import sys
sys.path.insert(1, '/home/plof/Documents/PythonProjects/sovl/souvl_lib')
from PyQt5.QtWidgets import QApplication, QPushButton, QSlider
from PyQt5.QtCore import Qt
app = QApplication([])
import objects
import config

window=objects.window()
windowconfig, buttonsConfig, slidersConfig=config.read_config("/home/plof/.config/sovl/config.ini")
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


for j in slidersConfig:
    if j["position"]=="Horizontal":
        objects.Slider(QSlider(Qt.Orientation.Horizontal,window), j)
    elif j["position"]=="Vertical":
        objects.Slider(QSlider(Qt.Orientation.Vertical,window), j)
    else:
        print("Position not defined")


window.show()
app.exec()
sys.exit(objects.StopTheProcess.set())
