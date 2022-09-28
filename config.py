import configparser
from PIL import Image
import os 


path_config=str(os.getenv("HOME"))+"/.config/sovl/"


def read_config(path):

    buttons=[]

    window={"X":10,"Y":10,"Height":10,"Width":10,"Image":"Default.jpg"}
    config = configparser.ConfigParser()
    config.read(path)
    
    try:
        window["X"]=int(config["Window"]["X"])
        window["Y"]=int(config["Window"]["Y"])
        window["Height"]=int(config["Window"]["Height"])
        window["Width"]=int(config["Window"]["Width"])
        window["Image"]=config["Window"]["Func"]
    except:
        pass 

    for i in config.sections():
        if i=="Window":
            continue
        buton={"x":10,"y":10,"height":10,"width":10,"func":"play","shape":"Default"}
        for j in config[i]:
            buton[j]=config[i][j]
        buttons.append(buton)

    return window,buttons

def image_resize(image,height,withd):
    img=Image.open(image)
    new_img=img.resize((height,withd))
    new_img_path=path_config+"resized"+image
    new_img.save(new_img_path)
    return(new_img_path)

def config_exist():
    path=path_config+"config.ini"
    if os.path.exists(path):
        window_config,buttons_config=read_config(path)
    else:
        os.system("mkdir ~/.config/sovl")
        os.system("touch ~/.config/sovl/config.ini")
        f = open(path, "a")
        f.write("[Window]")
        f.close()
        window_config,buttons_config=read_config(path)
    return window_config,buttons_config


def image_config(window_config):
    image_already_rezised=path_config+"resized"+window_config["Image"]
    if os.path.exists(image_already_rezised):
        window_config["Image"]=image_already_rezised
    else:
        image_resize(window_config["Image"],window_config["Height"],window_config["Width"])
        window_config["Image"]=image_already_rezised
    return image_already_rezised
