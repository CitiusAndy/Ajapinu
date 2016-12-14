#Import statements
import pygame
from time import time
from Scrambles import generate3x3Scramble
from Averages import calculateAverage, calculateMean, calculateBest, calculateWorst

#Constants
displayWidth=1200
displayHeight=800
WHITE=(255,255,255)
BLACK=(0,0,0)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)
YELLOW=(255,255,0)
ORANGE=(255,128,0)


#Displaying functions
def displayTimer(solveTime):
    """
    Displays current solving time.
    Args: solvetime
    Returns: displays the solve time
    """
    solveTime = str(solveTime)
    timeFont = pygame.font.SysFont("Arial", 72)
    textPicture = timeFont.render(solveTime, False, BLACK, WHITE)
    appDisplay.blit(textPicture, (displayWidth/2-72, displayHeight/2-72))

def displayScramble(scramble): #displays the current scramble on the screen
    text = ""
    for move in scramble:
        text += " "+move
    text = "Scramble:" + text
    scrambleFont = pygame.font.SysFont("Arial",25)
    scramblePicture = scrambleFont.render(text, False, BLACK, WHITE)
    appDisplay.blit(scramblePicture, (20,30))

def displayBest(bestTime):
    """
    Displays the best time in green colour.
    Args: the best solving time
    Returns: displays the best solving time
    """
    bestTime = "Best:   " + str(bestTime)
    bestFont = pygame.font.SysFont("Arial", 30)
    bestPicture = bestFont.render(bestTime, False, GREEN, WHITE)
    appDisplay.blit(bestPicture, (900,60))

def displayWorst(worstTime):
    """
    Displays the worst time in red colour.
    Args: the worst solving time
    Returns: displays the worst solving time
    """
    worstTime = "Worst: " + str(worstTime)
    worstFont = pygame.font.SysFont("Arial", 30)
    worstPicture = worstFont.render(worstTime, False, RED, WHITE)
    appDisplay.blit(worstPicture, (900,90))

def displayUniversal(name, value, width, height):
    """
    A universal function for displaying various texts on the display.
    
    Args:
    
        name: the essence of what is going to be displayed, for example: mean, average
        value: the numerical value to be displayed on the screen
        width: number of pixels in width
        height: number of pixels in height
        
    Returns: displays information in format name+value in its correct location
    """
    text = name + str(value)
    universalFont = pygame.font.SysFont("Arial", 30)
    universalPicture = universalFont.render(text, False, BLACK, WHITE)
    appDisplay.blit(universalPicture, (width, height))


"""Modelling the cube"""
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
    
"""Following functions are for modelling the cube"""
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

"""Main program"""

#Initializing and setting important variables
pygame.init()
appDisplay=pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption("Ajapinu")
clock=pygame.time.Clock()
appDisplay.fill(WHITE)


#Displaying the timer
solveTime="0.00"
displayTimer(solveTime)

#Displaying the scramble
scramble = generate3x3Scramble(22)
displayScramble(scramble)

#Displaying the cube picture
front,up,right,left,down,back = getCube()
scrambleCube(scramble)
drawCube(100,300,30)

#Displaying statistics
displayUniversal("Solves: ", "", 900, 30)
displayBest("")
displayWorst("")
displayUniversal("Mean: ", "", 900, 120)

#Initializing important variables
timerRunning=False
beginTime=0
solves=0
times=[]

"""Main loop"""
while True:
    
    #Update the display and set fps
    pygame.display.update()
    clock.tick(60)
    
    #Getting events
    for event in pygame.event.get():
        
        #Pressing the close button
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
            
        #Pressing any key    
        if event.type == pygame.KEYDOWN:
            
            #Starting the timer
            if event.key==pygame.K_SPACE and not timerRunning:
                beginTime=time()
                timerRunning=True
                solves+=1
                
            #Stopping the timer    
            elif event.key==pygame.K_SPACE and timerRunning:
                timerRunning=False

    #Updating the solving time
    if timerRunning:
        solveTime="%.2f" % round(time()-beginTime, 2)

    #The timer has been in use
    if not timerRunning and beginTime!=0:
        
        #If a new solve has been added
        if len(times)!=solves:
            appDisplay.fill(WHITE)
            times.append(float(solveTime))

            #New scramble generation and displaying
            scramble = generate3x3Scramble(22)
            displayScramble(scramble)

            #New cube picture displaying
            front,up,right,left,down,back = getCube()
            scrambleCube(scramble)
            drawCube(100,300,30)

            #Updating statistics values
            displayUniversal("Solves: ", solves, 900, 30)
            displayBest(calculateBest(times))
            displayWorst(calculateWorst(times))
            displayUniversal("Mean: ", calculateMean(times), 900, 120)
            
            if len(times)>=5:
                displayUniversal("Average of 5: ", calculateAverage(times, solves-5, solves), 900, 150)
                
            if len(times)>=12:
                displayUniversal("Average of 12: ", calculateAverage(times, solves-12, solves), 900, 185)
                
            displayUniversal("Times: ", "", 1000, 215)

            sliceList = times[-18:]
            for timeIndex in range(len(sliceList)):
                displayUniversal('', '%.2f' % sliceList[timeIndex], 1000, 245+30*timeIndex)
                
    #Display the current solving time
    displayTimer(solveTime)
    
pygame.quit()
quit()
   
