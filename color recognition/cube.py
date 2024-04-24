import numpy as np

class Cube:
    def __init__(self):
        self.Wx = np.array([['W', 'W', 'W'], ['W', 'W', 'W'], ['W', 'W', 'W']])
        self.Rx = np.array([['R', 'R', 'R'], ['R', 'R', 'R'], ['R', 'R', 'R']])
        self.Bx = np.array([['B', 'B', 'B'], ['B', 'B', 'B'], ['B', 'B', 'B']])
        self.Ox = np.array([['O', 'O', 'O'], ['O', 'O', 'O'], ['O', 'O', 'O']])
        self.Gx = np.array([['G', 'G', 'G'], ['G', 'G', 'G'], ['G', 'G', 'G']])
        self.Yx = np.array([['Y', 'Y', 'Y'], ['Y', 'Y', 'Y'], ['Y', 'Y', 'Y']])
        self.CV = [0,0,-1]
        self.frontFace = [0,0,-1]
    def showCube(self):
        print("Front face: " + str(self.frontFace))
        print(15 * "_")
        print(np.array(self.Wx))
        print("_ _ _ _")
        print(np.array(self.Rx))
        print("_ _ _ _")
        print(np.array(self.Bx))
        print("_ _ _ _")
        print(np.array(self.Ox))
        print("_ _ _ _")
        print(np.array(self.Gx))
        print("_ _ _ _")
        print(np.array(self.Yx))

cubo = Cube()

def faceRotation(current, rot, axis):
    if rot == 90:
        sin = 1
        cos = 0
    elif rot == -90:
        sin = -1
        cos = 0
    elif rot == 180:
        sin = 0
        cos = -1
        
    x = current[0]
    y = current[1]
    z = current[2]
    
    if axis == "X":
        x_ = x
        y_ =(y * cos) - (z * sin)
        z_ = (y * sin) + (z * cos)
        
    elif axis == "Y":
        x_ = (x * cos) + (z * sin)
        y_ = y
        z_ = (-x * sin) + (z * cos)
        
    elif axis == "Z":
        x_ = (x * cos) - (y * sin)
        y_ = (x * sin) + (y * cos)
        z_ = z
    return [x_, y_, z_]

def getFaceConfig(vector):
    if vector == [0, 1, 0]:
        face = cubo.Wx
    elif vector == [0, 0, -1]:
        face = cubo.Gx
    elif vector == [-1, 0, 0]:
        face = cubo.Ox
    elif vector == [0, 0, 1]:
        face = cubo.Bx
    elif vector == [1, 0, 0]:
        face = cubo.Rx
    elif vector == [0, -1, 0]:
        face = cubo.Yx   
    return face

def YRot(vector):
    count = 0
    while True:
        if vector == cubo.CV:
            return count
        else:
            vector = faceRotation(vector, 90, "Y")
            #print(cubo.CV)
            count += 1

def confReplacement(vector, newConf):
    if vector == [0, 1, 0]:
        cubo.Wx = newConf
    elif vector == [0, 0, -1]:
        cubo.Gx = newConf
    elif vector == [-1, 0, 0]:
        cubo.Ox = newConf
    elif vector == [0, 0, 1]:
        cubo.Bx = newConf
    elif vector == [1, 0, 0]:
        cubo.Rx = newConf
    elif vector == [0, -1, 0]:
        cubo.Yx = newConf

### MOVES ###
# THREE TYPES: SIDEMOVE, UPPERMOVE, DOWNMOVE

def sideMove(vector):
    if cubo.CV == 0:
        cubo.CV = vector

    if vector[1] == 0:
        if vector[0] != 0:
            axis = "Z"
        elif vector[0] == 0:
            axis = "X"
        if vector[0] == -1 or vector[2] == 1:
            mult = -1
        else:
            mult = 1

        upFace = faceRotation(vector, 90 * mult, axis)
        rightFace = faceRotation(vector, -90, "Y")
        downFace = faceRotation(vector, -90 * mult, axis)
        leftFace = faceRotation(vector, 90, "Y")

        vectorConf = getFaceConfig(vector)
        upConf = getFaceConfig(upFace)
        rightConf = getFaceConfig(rightFace)
        downConf = getFaceConfig(downFace)
        leftConf = getFaceConfig(leftFace)

        newUp = np.rot90(upConf, k=-1 * (YRot(vector)))
        newDown = np.rot90(downConf, k=1 * (YRot(vector)))

        lftmov = (leftConf[0][2], leftConf[1][2], leftConf[2][2])
        upmov = (newUp[2][0], newUp[2][1], newUp[2][2])
        rghtmov = (rightConf[0][0], rightConf[1][0], rightConf[2][0])
        dwnmov = (newDown[0][0], newDown[0][1], newDown[0][2])

        newConfLeft = [[leftConf[0][0], leftConf[0][1], dwnmov[0]],
                       [leftConf[1][0], leftConf[1][1], dwnmov[1]],
                       [leftConf[2][0], leftConf[2][1], dwnmov[2]]]
        
        newConfUp = [[newUp[0][0], newUp[0][1], newUp[0][2]],
                     [newUp[1][0], newUp[1][1], newUp[1][2]],
                     [lftmov[2], lftmov[1], lftmov[0]]]

        newConfRight = [[upmov[0], rightConf[0][1], rightConf[0][2]],
                        [upmov[1], rightConf[1][1], rightConf[1][2]],
                        [upmov[2], rightConf[2][1], rightConf[2][2]]]

        newConfDown = [[rghtmov[2], rghtmov[1], rghtmov[0]],
                       [newDown[1][0], newDown[1][1], newDown[1][2]],
                       [newDown[2][0], newDown[2][1], newDown[2][2]]]

        newConfvector = np.rot90(vectorConf, k=-1)
        
        confReplacement(upFace, newConfUp)
        confReplacement(leftFace, newConfLeft)
        confReplacement(rightFace, newConfRight)
        confReplacement(downFace, newConfDown)
        confReplacement(vector, newConfvector)
        
        cubo.CV = vector
        
def upperMove(vector):
    if cubo.CV == 0:
        cubo.CV = vector
    
    if vector[1] == 0:
        if vector[0] != 0:
            axis = "Z"
        elif vector[0] == 0:
            axis = "X"
        if vector[0] == -1 or vector[2] == 1:
            mult = -1
        else:
            mult = 1

        upFace = faceRotation(vector, 90 * mult, axis)
        rightFace = faceRotation(vector, -90, "Y")
        backFace = faceRotation(vector, 180, "Y")
        leftFace = faceRotation(vector, 90, "Y")
        downFace = faceRotation(vector, -90 * mult, axis)
        
        vectorConf = getFaceConfig(vector)
        upConf = getFaceConfig(upFace)
        rightConf = getFaceConfig(rightFace)
        backConf = getFaceConfig(backFace)
        leftConf = getFaceConfig(leftFace)
        downConf = getFaceConfig(downFace)
        
        newUp = np.rot90(upConf, k=-1 * (YRot(vector)))
        newConfDown = np.rot90(downConf, k=1 * (YRot(vector)))
       
        frntmov = (vectorConf[0][0], vectorConf[0][1], vectorConf[0][2])
        rghtmov = (rightConf[0][0],rightConf[0][1],rightConf[0][2])
        backmov = (backConf[0][0],backConf[0][1],backConf[0][2])
        lftmov = (leftConf[0][0],leftConf[0][1],leftConf[0][2])
        
        newConfUp = np.rot90(newUp, k=-1)
        
        newConfLeft = (frntmov, leftConf[1], leftConf[2])
        newConfLeft = np.array(newConfLeft)
        
        
        newConfBack = (lftmov, backConf[1], backConf[2])
        newConfBack = np.array(newConfBack)
        
        
        newConfRight = (backmov, rightConf[1], rightConf[2])
        newConfRight = np.array(newConfRight)
        
        
        newConfFront = (rghtmov, vectorConf[1], vectorConf[2])
        newConfFront = np.array(newConfFront)
        
        confReplacement(upFace, newConfUp)
        confReplacement(leftFace, newConfLeft)
        confReplacement(rightFace, newConfRight)
        confReplacement(downFace, newConfDown)
        confReplacement(vector, newConfFront)
        confReplacement(backFace, newConfBack)
        
        cubo.CV = vector

def downMove(vector):
    if cubo.CV == 0:
        cubo.CV = vector
    
    if vector[1] == 0:
        if vector[0] != 0:
            axis = "Z"
        elif vector[0] == 0:
            axis = "X"
        if vector[0] == -1 or vector[2] == 1:
            mult = -1
        else:
            mult = 1

        upFace = faceRotation(vector, 90 * mult, axis)
        rightFace = faceRotation(vector, -90, "Y")
        backFace = faceRotation(vector, 180, "Y")
        leftFace = faceRotation(vector, 90, "Y")
        downFace = faceRotation(vector, -90 * mult, axis)
        
        vectorConf = getFaceConfig(vector)
        upConf = getFaceConfig(upFace)
        rightConf = getFaceConfig(rightFace)
        backConf = getFaceConfig(backFace)
        leftConf = getFaceConfig(leftFace)
        downConf = getFaceConfig(downFace)
        
        newConfUp = np.rot90(upConf, k=-1 * (YRot(vector)))
        newDown = np.rot90(downConf, k=1 * (YRot(vector)))
        
        newConfDown = np.rot90(newDown, k=-1)
        
        frntmov = (vectorConf[2][0],vectorConf[2][1],vectorConf[2][2])
        lftmov = (leftConf[2][0], leftConf[2][1], leftConf[2][2])
        backmov = (backConf[2][0],backConf[2][1],backConf[2][2])
        rghtmov = (rightConf[2][0],rightConf[2][1],rightConf[2][2] )
        
        newConfRight = (rightConf[0], rightConf[1], frntmov)
        newConfRight = np.array(newConfRight)
        
        newConfBack = (backConf[0], backConf[1], rghtmov)
        newConfBack = np.array(newConfBack)
        
        newConfLeft = (leftConf[0], leftConf[1], backmov)
        newConfLeft = np.array(newConfLeft)
        
        newConfFront = (vectorConf[0], vectorConf[1], lftmov)
        newConfFront = np.array(newConfFront)
    
        confReplacement(upFace, newConfUp)
        confReplacement(leftFace, newConfLeft)
        confReplacement(rightFace, newConfRight)
        confReplacement(downFace, newConfDown)
        confReplacement(vector, newConfFront)
        confReplacement(backFace, newConfBack) 

        cubo.CV = vector

### CUBE MANIPULATION ###

def switchFrontFaceTo(vector):
    cubo.frontFace = vector

def F(times=1):
    for i in range(times):
        sideMove(cubo.frontFace)

def F_(times=1):
    for i in range(times):
        for j in range(3):
            F()

def R (times=1):
    for i in range(times):
        rightFace = faceRotation(cubo.frontFace, -90, "Y")
        sideMove(rightFace)

def R_ (times=1):
    for i in range(times):
        for j in range(3):
            R()

def L (times=1):
    for i in range(times):
        leftFace = faceRotation(cubo.frontFace, 90, "Y")
        sideMove(leftFace)

def L_ (times=1):
    for i in range(times):
        for j in range(3):
            L()

def U (times=1):
    for i in range(times):
        upperMove(cubo.frontFace)

def U_ (times=1):
    for i in range(times):
        for j in range(3):
            U()

def B (times=1):
    for i in range(times):
        backFace = faceRotation(cubo.frontFace, 180, "Y")
        sideMove(backFace)

def B_ (times=1):
    for i in range(times):
        for j in range(3):
            B()

def D (times=1):
    for i in range(times):
        downMove(cubo.frontFace)

def D_ (times=1):
    for i in range(times):
        for j in range(3):
            D()
