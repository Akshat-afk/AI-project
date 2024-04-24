import cv2

def color_reader(h,s):
    color = "U"
    if h >= 0 and h <= 10 and s > 100 and s <= 255:
        color = "R"
    elif h>10 and h<=25 and s > 100 and s <= 255:
        color = "O"
    elif h>25 and h<=40 and s > 100 and s <= 255:
        color = "Y"
    elif h>35 and h<=75 and s > 100 and s <= 255:
        color = "G"
    elif h>75 and h<130 and s > 100 and s <= 255:
        color = "B"
    elif s < 100:
        color = "W"
    else: 
        color = "U"
    return color

def color2rgb (color):
    if color == "R":
        rgb = (0, 0, 255)
    elif color == "O":
        rgb = (0, 100, 255)
    elif color == "Y":
        rgb = (0, 255, 255)
    elif color == "G":
        rgb = (0, 210, 100)
    elif color == "B":
        rgb = (219, 70, 29)
    elif color == "W":
        rgb = (255, 255, 255)
    else:
        rgb = (0,0,0)
    return rgb

def face_color (center):
    h = center[0]
    s = center[1]
    color = color_reader(h,s)
    return color

def input(face_color):
    if face_color == "W":
        None