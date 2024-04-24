import numpy as np
import cv2
import functions as func

class cubes_face():
    def __init__(self, color):
        self.face = np.array([['WHITE', 'WHITE', 'WHITE'], ['WHITE', 'WHITE', 'WHITE'], ['WHITE', 'WHITE', 'WHITE']])
        self.color = color
    
    def replace(self, upLeft, up, upRight, left, center, right, downLeft, down, downRight):
        a = func.color_reader(upLeft[0], upLeft[1])
        b = func.color_reader(up[0], up[1])
        c = func.color_reader(upRight[0], upRight[1])
        d = func.color_reader(left[0], left[1])
        e = func.color_reader(center[0], center[1])
        f = func.color_reader(right[0], right[1])
        g = func.color_reader(downLeft[0], downLeft[1])
        h = func.color_reader(down[0], down[1])
        i = func.color_reader(downRight[0], downRight[1])
        self.face = np.array([[a, b, c], [d, e, f], [g, h, i]])
        print("New face configuration for: " + self.color)
        print(self.face)
        return (np.array([[a,b,c], [d,e,f], [g,h,i]]))
    
    def schema(self, frame, X, Y, upLeft, up, upRight, left, center, right, downLeft, down, downRight):
        array = self.face
        if func.color_reader(center[0], center[1]) == self.color:
            cv2.rectangle(frame, (X - 30, Y - 30), (X - 10, Y - 10), (func.color2rgb(func.color_reader(upLeft[0], upLeft[1]))), -1 )
            cv2.rectangle(frame, (X, Y - 30), (X + 20, Y - 10), (func.color2rgb(func.color_reader(up[0], up[1]))), -1 )
            cv2.rectangle(frame, (X + 30, Y - 30), (X + 50, Y - 10), (func.color2rgb(func.color_reader(upRight[0], upRight[1]))), -1 )

            cv2.rectangle(frame, (X - 30, Y), (X - 10, Y  + 20), (func.color2rgb(func.color_reader(left[0], left[1]))), -1 )
            cv2.rectangle(frame, (X, Y), (X + 20, Y  + 20), (func.color2rgb(self.color)), -1)
            cv2.rectangle(frame, (X + 30, Y), (X + 50, Y  + 20), (func.color2rgb(func.color_reader(right[0], right[1]))), -1 )

            cv2.rectangle(frame, (X - 30, Y + 30), (X - 10, Y  + 50), (func.color2rgb(func.color_reader(downLeft[0], downLeft[1]))), -1 )
            cv2.rectangle(frame, (X, Y + 30), (X + 20, Y  + 50), (func.color2rgb(func.color_reader(down[0], down[1]))), -1 )
            cv2.rectangle(frame, (X + 30, Y + 30), (X + 50, Y  + 50), (func.color2rgb(func.color_reader(downRight[0], downRight[1]))), -1 )
        else:
            cv2.rectangle(frame, (X - 30, Y - 30), (X - 10, Y - 10), (func.color2rgb(array[0][0])), -1 )
            cv2.rectangle(frame, (X, Y - 30), (X + 20, Y - 10), (func.color2rgb((array[0][1]))), -1 )
            cv2.rectangle(frame, (X + 30, Y - 30), (X + 50, Y - 10), (func.color2rgb((array[0][2]))), -1 )

            cv2.rectangle(frame, (X - 30, Y), (X - 10, Y  + 20), (func.color2rgb((array[1][0]))), -1 )
            cv2.rectangle(frame, (X, Y), (X + 20, Y  + 20), (func.color2rgb(self.color)), -1)
            cv2.rectangle(frame, (X + 30, Y), (X + 50, Y  + 20), (func.color2rgb((array[1][2]))), -1 )

            cv2.rectangle(frame, (X - 30, Y + 30), (X - 10, Y  + 50), (func.color2rgb((array[2][0]))), -1 )
            cv2.rectangle(frame, (X, Y + 30), (X + 20, Y  + 50), (func.color2rgb((array[2][1]))), -1 )
            cv2.rectangle(frame, (X + 30, Y + 30), (X + 50, Y  + 50), (func.color2rgb((array[2][2]))), -1 )
            