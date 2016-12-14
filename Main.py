#Import statements
import pygame
from time import time
from Averages import calculateAverage, calculateMean, calculateBest, calculateWorst
from Cube import *
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

def displayUniversal(name, value, width, height, fontSize=30):
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
    universalFont = pygame.font.SysFont("Arial", fontSize)
    universalPicture = universalFont.render(text, False, BLACK, WHITE)
    appDisplay.blit(universalPicture, (width, height))

"""Displaying the cube"""
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
scrambleCube(scramble,[front,up,right,left,down,back])
drawCube(100,300,30)

#Displaying statistics
displayUniversal("Solves: ", "", 900, 30)
displayBest("")
displayWorst("")
displayUniversal("Mean: ", "", 900, 120)

#Initializing important variables
timerRunning=False
displayPreviousScramble=False
previousScramble=""
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

            #For displaying previous scramble
            if event.key==pygame.K_BACKSPACE and previousScramble != "":
                displayPreviousScramble=True

    #Updating the solving time
    if timerRunning:
        solveTime="%.2f" % round(time()-beginTime, 2)

    #The timer has been in use
    if not timerRunning and beginTime != 0:
        
        #If backspace is pressed
        if displayPreviousScramble:
            displayUniversal("Previous scramble: ", " ".join(previousScramble), 20, 60, 25)
            displayPreviousScramble=False
        
        #If a new solve has been added
        if len(times) != solves:
            appDisplay.fill(WHITE)
            times.append(float(solveTime))

            #New scramble generation and displaying
            previousScramble = scramble
            scramble = generate3x3Scramble(22)
            displayScramble(scramble)


            
            #New cube picture displaying
            front,up,right,left,down,back = getCube()
            scrambleCube(scramble,[front,up,right,left,down,back])
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
   
