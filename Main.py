import pygame
from time import time
from Scrambles import generate3x3Scramble
from Averages import calculateAverage, calculateMean, calculateBest, calculateWorst

pygame.init()

displayWidth=1200
displayHeight=800
WHITE=(255,255,255)
BLACK=(0,0,0)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)
YELLOW=(255,255,0)
ORANGE=(255,128,0)

appDisplay=pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption("Ajapinu")
clock=pygame.time.Clock()
appDisplay.fill(WHITE)

def displayTime(text):
    text = str(text)
    timeFont = pygame.font.SysFont("Arial", 72)
    textPicture = timeFont.render(text, False, BLACK, WHITE)
    appDisplay.blit(textPicture, (displayWidth/2-72, displayHeight/2-72))

def displayScramble(scramble): #displays the current scramble on the screen
    text = ""
    for move in scramble:
        text += " "+move
    text = "Scramble:" + text
    scrambleFont = pygame.font.SysFont("Arial",25)
    scramblePicture = scrambleFont.render(text, False, BLACK, WHITE)
    appDisplay.blit(scramblePicture, (20,30))

def displaySolveNumber(text):
    text = "Solves: " + str(text)
    solveNumberFont = pygame.font.SysFont("Arial", 30)
    solveNumberPicture = solveNumberFont.render(text, False, BLACK, WHITE)
    appDisplay.blit(solveNumberPicture, (900,30))

def displayBest(text):
    text = "Best:   " + str(text)
    bestFont = pygame.font.SysFont("Arial", 30)
    bestPicture = bestFont.render(text, False, BLACK, WHITE)
    appDisplay.blit(bestPicture, (900,60))

def displayWorst(text):
    text = "Worst: " + str(text)
    worstFont = pygame.font.SysFont("Arial", 30)
    worstPicture = worstFont.render(text, False, BLACK, WHITE)
    appDisplay.blit(worstPicture, (900,90))

def displayMean(text):
    text = "Mean: " + str(text)
    meanFont = pygame.font.SysFont("Arial", 30)
    meanPicture = meanFont.render(text, False, BLACK, WHITE)
    appDisplay.blit(meanPicture, (900, 120))
    
def displayAo5(text):
    text = "Average of 5: " + str(text)
    ao5Font = pygame.font.SysFont("Arial", 30)
    ao5Picture = ao5Font.render(text, False, BLACK, WHITE)
    appDisplay.blit(ao5Picture, (900, 150))

def displayAo12(text):
    text = "Average of 12: " + str(text)
    ao12Font = pygame.font.SysFont("Arial", 30)
    ao12Picture = ao12Font.render(text, False, BLACK, WHITE)
    appDisplay.blit(ao12Picture, (900, 185))

def getColour(sticker): ##returns the color of the sticker being looked at    
    if sticker == "g":
        return GREEN
    if sticker == "r":
        return RED
    if sticker == "b":
        return BLUE
    if sticker == "w":
        return WHITE
    if sticker == "y":
        return YELLOW
    if sticker == "o":
        return ORANGE
    
def drawFace(x,y,length,face): #draws one face of the cube at coordinates x,y (upper left corner)
    for dy,row in enumerate(face):
        for dx,sticker in enumerate(row):
            pygame.draw.rect(appDisplay, getColour(sticker),(x+dx*length,y+dy*length,length,length))
            pygame.draw.rect(appDisplay, BLACK,(x+dx*length,y+dy*length,length,length),5)

#draws all of the faces of the cube,length is the sidelength of one sticker
#x,y is the upper left corner of the "rectangle" that contains the picture of the scramble
def drawCube(x,y,length): 
    drawFace(x,y+length*3,length,left)
    drawFace(x+length*3,y+length*3,length,front)
    drawFace(x+length*6,y+length*3,length,right)
    drawFace(x+length*9,y+length*3,length,back)
    drawFace(x+length*3,y,length,up)
    drawFace(x+length*3,y+length*6,length,down)
    
########### Following functions are for modelling the cube
##generates the 6 faces of a rubik's cube; all faces are represented by a 3x3 list of single character strings, which correspond to colours
##g-green;w-white;r-red;o-orange;y-yellow;b-blue
def getCube():  
    front = [["g" for i in range(3)] for j in range(3)]
    up = [["w" for i in range(3)] for j in range(3)]
    right = [["r" for i in range(3)] for j in range(3)]
    left = [["o" for i in range(3)] for j in range(3)]
    down = [["y" for i in range(3)] for j in range(3)]
    back = [["b" for i in range(3)] for j in range(3)]
    return front,up,right,left,down,back

def rotate(face,i): ##rotates the stickers on one face; clockwise 90 degrees if i=1, 180 degrees if i=2 and 90 degrees counter-clockwise if i=-1
    if i == "1":
        face[0][1],face[1][0],face[2][1],face[1][2] = face[1][0],face[2][1],face[1][2],face[0][1]
        face[0][0],face[2][0],face[2][2],face[0][2] = face[2][0],face[2][2],face[0][2],face[0][0]
    elif i == "2":
        rotate(face,"1")
        rotate(face,"1")
    elif i == "'":
        rotate(face,"1")
        rotate(face,"1")
        rotate(face,"1")

def getRow(face,n,i=1): #returns the n-th row of a face; returns it reversed if i = 0
    if i:
        return [face[0][n],face[1][n],face[2][n]]
    else:
        return [face[2][n],face[1][n],face[0][n]]

def replaceRow(row,face,n): #replaces the n-th row of a face with the list row
    for i in range(3):
        face[i][n] = row[i]

##Note: the following functions are named with uppercase letters
##      as they correspond to specific turns on the cube which are commonly denoted with uppercase letters
        
def U(i): #defines the movement of the upper layer
    if i == "1":
        rotate(up,"1")
        front[0],right[0],back[0],left[0] = right[0],back[0],left[0],front[0]
    elif i == "2":
        U("1");U("1")
    elif i == "'":
        rotate(up,"'")
        front[0],left[0],back[0],right[0] = left[0],back[0],right[0],front[0]

def D(i): #defines the movement of the bottom layer
    if i == "1":
        rotate(down,"1")
        front[2],left[2],back[2],right[2] = left[2],back[2],right[2],front[2]              
    elif i == "2":
        D("1");D("1")
    elif i == "'":
        rotate(down,"'")
        front[2],right[2],back[2],left[2]=right[2],back[2],left[2],front[2]

def R(i): #defines the movement of the right layer
    if i == "1":
        rotate(right,"1")
        temp = getRow(up,2,0)
        replaceRow(getRow(front,2),up,2)
        replaceRow(getRow(down,2),front,2)
        replaceRow(getRow(back,0,0),down,2)
        replaceRow(temp,back,0)
    elif i == "2":
        R("1");R("1")
    elif i == "'":
        R("1");R("1");R("1") ##for simplicity, a counter-clockwise turn is defined as 3 turns clockwise

def L(i): #defines the movement of the left layer
    if i == "1":
        rotate(left,"1")
        temp = getRow(up,0)
        replaceRow(getRow(back,2,0),up,0)
        replaceRow(getRow(down,0,0),back,2)
        replaceRow(getRow(front,0),down,0)
        replaceRow(temp,front,0)
    elif i == "2":
        L("1");L("1")
    elif i == "'":
        L("1");L("1");L("1")

def F(i): #defines the movement of the front layer
    if i == "1":
        rotate(front,"1")
        temp = up[2]
        up[2] = getRow(left,2,0)
        replaceRow(down[0],left,2)
        down[0] = getRow(right,0,0)
        replaceRow(temp,right,0)
    elif i == "2":
        F("1");F("1")
    elif i == "'":
        F("1");F("1");F("1")

def B(i): #defines the movement of the back layer
    if i == "1":
        rotate(back,"1")
        temp = list(reversed(up[0]))
        up[0] = getRow(right,2)
        replaceRow(list(reversed(down[2])),right,2)
        down[2] = getRow(left,0)
        replaceRow(temp,left,0)
    elif i == "2":
        B("1");B("1")
    elif i == "'":
        B("1");B("1");B("1")


def scrambleCube(scramble):
    for move in scramble:
        
        if len(move) == 1:
            move+="1"
 
        if move[0] == "F":
            F(move[1])
        elif move[0] == "U":
            U(move[1])
        elif move[0] == "R":
            R(move[1])
        elif move[0] == "L":
            L(move[1])
        elif move[0] == "D":
            D(move[1])
        elif move[0] == "B":
            B(move[1])            

############ modelling the cube ends here

solveTime="0.00"
displayTime(solveTime)

scramble = generate3x3Scramble(25)
displayScramble(scramble)

front,up,right,left,down,back = getCube()
scrambleCube(scramble)
drawCube(100,300,30)

displaySolveNumber("")
displayBest("")
displayWorst("")
displayMean("")

timerRunning=False
beginTime=0
times=[]
solves=0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_SPACE and not timerRunning:
                beginTime=time()
                timerRunning=True
                solves+=1
            elif event.key==pygame.K_SPACE and timerRunning:
                timerRunning=False

    if timerRunning:
        solveTime="%.2f" % round(time()-beginTime, 2)

    if not timerRunning and beginTime!=0:
        if len(times)!=solves:
            appDisplay.fill(WHITE)
            times.append(float(solveTime))
            
            scramble = generate3x3Scramble(25)
            displayScramble(scramble)
            
            front,up,right,left,down,back = getCube()
            scrambleCube(scramble)
            drawCube(100,300,30)

            displaySolveNumber(solves)
            displayBest(calculateBest(times))
            displayWorst(calculateWorst(times))
            displayMean(calculateMean(times))

            if len(times)>=5:
                displayAo5(calculateAverage(times, solves-5, solves))
            if len(times)>=12:
                displayAo12(calculateAverage(times, solves-12, solves))
            
    displayTime(solveTime)

    pygame.display.update()
    clock.tick(60)


quit()
pygame.quit()
   
