import os
from PIL import Image
import subprocess

def status():
    status=subprocess.run(['mpc','status'],stdout=subprocess.PIPE)
    return status.stdout.decode('utf-8')


def play_pause():
    os.system("mpc toggle")

def prev():
    os.system("mpc prev")

def next():
    os.system("mpc next")

def stop():
    os.system("mpc prev")

def random():
    os.system("mpc random")

def shuffle():
    os.system("mpc shuffle")

def image_resize(height,width, image):
    img=Image.open(image)
    newimg=img.resize((height,width))
    newimg.save("resized"+image)

def image_size(image):
    img=Image.open(image)
    return(img.size)
