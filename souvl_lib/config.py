import configparser
from PIL import Image
import os 


path_config=str(os.getenv("HOME"))+"/.config/sovl/"


def read_config(path):

    buttons=[]
    sliders=[]

    window={"X":10,"Y":10,"Height":10,"Width":10,"Image":"Default.jpg","Icon":"Default.jpg"}
    config = configparser.RawConfigParser()
    config.read(path)
    window["X"]=int(config["Window"]["X"])
    window["Y"]=int(config["Window"]["Y"])
    window["Height"]=int(config["Window"]["Height"])
    window["Width"]=int(config["Window"]["Width"])
    window["Image"]=config["Window"]["Image"]
    window["Icon"]=config["Window"]["Icon"]

    for i in config.sections():
        if i.startswith("Button"):
            buton={"x":10,"y":10,"height":10,"width":10,"func":"play_pause","shape":"Default","image":"Default.png"}
            for j in config[i]:
                buton[j]=config[i][j]
            buttons.append(buton)
        elif i.startswith("Slider"):
            slider={"position":"Horizontal","x":10,"y":10,"height":40,"width":10,"func":"vol","color":None}
            for j in config[i]:
                slider[j]=config[i][j]
            sliders.append(slider)


    for i in buttons:
        i["x"]=int(i["x"])
        i["y"]=int(i["y"])
        i["height"]=int(i["height"])
        i["width"]=int(i["width"])

    for j in sliders:
        j["x"]=int(j["x"])
        j["y"]=int(j["y"])
        j["height"]=int(j["height"])
        j["width"]=int(j["width"])
        j["color"]=j["color"]

    return window,buttons,sliders

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
