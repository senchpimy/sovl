import configparser
from PIL import Image
import os 


path_config=str(os.getenv("HOME"))+"/.config/sovl/"


def read_config(path):

    buttons=[]

    window={"X":10,"Y":10,"Height":10,"Width":10,"Image":"Default.jpg","Icon":"Default.jpg"}
    config = configparser.RawConfigParser()
    config.read(path)
    window["X"]=int(config["Window"]["X"])
    window["Y"]=int(config["Window"]["Y"])
    window["Height"]=int(config["Window"]["Height"])
    window["Width"]=int(config["Window"]["Width"])
    window["Image"]=config["Window"]["Image"]
    window["Icon"]=config["Window"]["Icon"]
    
#    try:
#        window["X"]=int(config["Window"]["X"])
#        window["Y"]=int(config["Window"]["Y"])
#        window["Height"]=int(config["Window"]["Height"])
#        window["Width"]=int(config["Window"]["Width"])
#        window["Image"]=config["Window"]["Func"]
#        window["Icon"]=config["Window"]["Icon"]
#    except:
#        pass 

    for i in config.sections():
        if i=="Window":
            continue
        buton={"x":10,"y":10,"height":10,"width":10,"func":"play","shape":"Default","Image":"Default.png"}
        for j in config[i]:
            buton[j]=config[i][j]
        buttons.append(buton)

    return window,buttons

def image_resize(image,height,withd):
    img=Image.open(image)
    new_img=img.resize((height,withd))
    filename="".join(image.split("/")[-1:])
    new_img_path=path_config+"resized"+filename
    new_img.save(new_img_path)
    return(new_img_path)

def image_config(window_config):
    filename="".join(window_config["Image"].split("/")[-1:])
    image_already_rezised=path_config+"resized"+filename
    try:
        image_exist = Image.open(image_already_rezised)
        height,width= image_exist.size
    except:
        image_exist = False
        height, width= 0, 0

    if image_exist and height==window_config["Height"] and width==window_config["Width"]:
        window_config["Image"]=image_already_rezised
    else:
        image_resize(window_config["Image"],window_config["Height"],window_config["Width"])
        window_config["Image"]=image_already_rezised
    return image_already_rezised
