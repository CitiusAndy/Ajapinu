"""This file contains all functions necessary to model a 3x3 cube"""

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

#Generating 3x3 scrambles
from random import randint

def generate3x3Scramble(scrambleLength):
    """
    Generates WCA-style scramble with given scramble length.
    Args:
        scrambleLength: an integer of how long scramble is needed
    Returns:
        a list of the generated scramble
    """
    moves="UDFBLR"
    degrees=["", "'", "2"]
    scramble=[]
    previousMove=""
    
    for i in range(scrambleLength):
        randomMove=randint(0,5)
        randomDegree=randint(0,2)
        
        while previousMove==randomMove: #To check that no same layer moves are in sequence
            randomMove=randint(0,5) #Then generate a new face to move
        previousMove=randomMove
        
        scramble.append(moves[randomMove]+degrees[randomDegree])

    return scramble

#Scrambles the cube using the functions defined above
def scrambleCube(scramble,cube):

    #The following 2 lines make it possible for the function to access global variables from another file
    #These variables point to global variables in the main file but they are also globals in this module meaning they can be modified by functions defined here
    global front,up,right,left,down,back 
    front,up,right,left,down,back = cube[0],cube[1],cube[2],cube[3],cube[4],cube[5]
    
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

