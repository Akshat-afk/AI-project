import cv2
import functions as func
import classes as cls
import numpy as np
import cube 
def cube_scan():
    image = cv2.VideoCapture(0)

    white = cls.cubes_face("W")
    blue = cls.cubes_face("B")
    orange = cls.cubes_face("O")
    green = cls.cubes_face("G")
    red = cls.cubes_face("R")
    yellow = cls.cubes_face("Y")

    print("Rotate cube, press spacebar to save configuration for each face of the cube. Press esc to finish cube scan.")

    while True:
        _, frame = image.read()
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        height, width, _ = frame.shape

        centerX = int(width/2)
        centerY = int(height/2)

        upLeft = hsv_frame[centerY - 80, centerX - 80]
        up = hsv_frame[centerY - 80, centerX]
        upRight = hsv_frame[centerY - 80, centerX + 80]

        right = hsv_frame[centerY, centerX + 80]
        center = hsv_frame[centerY, centerX]
        left = hsv_frame[centerY, centerX - 80]

        downLeft = hsv_frame[centerY + 80, centerX - 80]
        down = hsv_frame[centerY + 80 , centerX]
        downRight = hsv_frame[centerY + 80, centerX + 80]
    
        face_color = func.face_color(center)
        cv2.putText(frame, (face_color + " FACE"), (200, 115), 0, 1, (func.color2rgb(face_color)), 2)

        white.schema(frame, 90, 100, upLeft, up, upRight, left, center, right, downLeft, down, downRight)
        blue.schema(frame, 90, 220, upLeft, up, upRight, left, center, right, downLeft, down, downRight)
        orange.schema(frame, 90, 340, upLeft, up, upRight, left, center, right, downLeft, down, downRight)
        green.schema(frame, 530, 100, upLeft, up, upRight, left, center, right, downLeft, down, downRight)
        red.schema(frame, 530, 220, upLeft, up, upRight, left, center, right, downLeft, down, downRight)
        yellow.schema(frame, 530, 340, upLeft, up, upRight, left, center, right, downLeft, down, downRight)
        cv2.rectangle(frame, (centerX-120, centerY-120), (centerX+120, centerY+120), (255, 255, 255), 1)
        cv2.imshow("Frame", frame)

        key = cv2.waitKey(1)
        if key == 27:
            break
        elif key == 32:
            if face_color == "W":
                conf = white.replace(upLeft, up, upRight, left, center, right, downLeft, down, downRight)
                cube.confReplacement(([0,1,0]), conf)
            elif face_color == "R":
                conf = red.replace(upLeft, up, upRight, left, center, right, downLeft, down, downRight)
                cube.confReplacement(([1,0,0]), conf)
            elif face_color == "B":
                conf = blue.replace(upLeft, up, upRight, left, center, right, downLeft, down, downRight)
                cube.confReplacement(([0,0,1]), conf)
            elif face_color == "G":
                conf = green.replace(upLeft, up, upRight, left, center, right, downLeft, down, downRight)
                cube.confReplacement(([0,0,-1]), conf)
            elif face_color == "O":
                conf = orange.replace(upLeft, up, upRight, left, center, right, downLeft, down, downRight)
                cube.confReplacement(([-1,0,0]), conf)
            elif face_color == "Y":
                conf = yellow.replace(upLeft, up, upRight, left, center, right, downLeft, down, downRight)
                cube.confReplacement(([0,-1,0]), conf)

    image.release()
    cv2.destroyAllWindows()