from PIL import Image
import cv2
import numpy as np
import cube
cubo = cube.cubo

img = cv2.imread('fondo.PNG', 1) 
def color_pick(color):
    if color == "W":
        rgb = (255, 255, 255)
    elif color == "G":
        rgb = (120, 240, 140)
    elif color == "R":
        rgb = (62, 74, 230)
    elif color == "B":
        rgb = (255, 61, 90)
    elif color == "O":
        rgb = (0, 109, 230)
    elif color == "Y":
        rgb = (53, 242, 238)
        
    return rgb

def color_list(array):
    colorlist = []
    for line in array:
        for item in line:
            colorlist.append(color_pick(item))
    return(colorlist)

def faceSchemaDraw(X, Y, color):
    cv2.rectangle(img, (X - 30, Y - 30), (X - 10, Y - 10), color[0], -1 )
    cv2.rectangle(img, (X, Y - 30), (X + 20, Y - 10), color[1], -1 )
    cv2.rectangle(img, (X + 30, Y - 30), (X + 50, Y - 10), color[2], -1 )

    cv2.rectangle(img, (X - 30, Y), (X - 10, Y  + 20), color[3], -1 )
    cv2.rectangle(img, (X, Y), (X + 20, Y  + 20), color[4], -1)
    cv2.rectangle(img, (X + 30, Y), (X + 50, Y  + 20), color[5], -1 )

    cv2.rectangle(img, (X - 30, Y + 30), (X - 10, Y  + 50), color[6], -1 )
    cv2.rectangle(img, (X, Y + 30), (X + 20, Y  + 50), color[7], -1 )
    cv2.rectangle(img, (X + 30, Y + 30), (X + 50, Y  + 50), color[8], -1 )

def corrector(vector):
    count = 0
    while True:
        if vector == cubo.frontFace:
            return count
        else:
            vector = cube.faceRotation(vector, 90, "Y")
            #print(cubo.CV)
            count += 1

def window_show():
    while True:
        cv2.imshow('image', img)
        #wcor = np.rot90(cubo.Wx, corrector(cubo.CV))
        print_cube()
        key = cv2.waitKey(1)
        if key == 27:
            break
        elif key == 108:
            cube.L()
            print("L")
        elif key == 107:
            cube.L_()
            print("L'")
        elif key == 114:
            cube.R()
            print("R")
        elif key == 116:
            cube.R_()
            print("R'")
        elif key == 117:
            cube.U()
            print("U")
        elif key == 121:
            cube.U_()
            print("U'")
        elif key == 100:
            cube.D()
            print("D")
        elif key == 115:
            cube.D_()
            print("D'")
        elif key == 98:
            cube.B()
            print("B")
        elif key == 118:
            cube.B_()
            print("B'")
        elif key == 102:
            cube.F()
            print("F")
        elif key == 103:
            cube.F_()
            print("F'")
        elif key == 49:
            cubo.frontFace = [0,0,-1]
            print("Front face changed to green")
        elif key == 50:
            cubo.frontFace = [1,0,0]
            print("Front face changed to red")
        elif key == 51:
            cubo.frontFace = [0,0,1]
            print("Front face changed to blue")
        elif key == 52:
            cubo.frontFace = [-1,0,0]
            print("Front face changed to orange")
        

    cv2.destroyAllWindows()

def print_cube():
    #GreenFace
    faceSchemaDraw(362, 238, color_list(cubo.Gx))
    #OrangeFace
    faceSchemaDraw(262, 238, color_list(cubo.Ox))
    #BlueFace
    faceSchemaDraw(162, 238, color_list(cubo.Bx))
    #RedFace
    faceSchemaDraw(462, 238, color_list(cubo.Rx))
    #WhiteFace
    faceSchemaDraw(362, 138, color_list(np.rot90(cubo.Wx, corrector(cubo.CV))))
    #YellowFace
    faceSchemaDraw(362, 338, color_list(np.rot90(cubo.Yx, -1 * corrector(cubo.CV))))

def see_cube ():
    print_cube()
    window_show()

#see_cube()