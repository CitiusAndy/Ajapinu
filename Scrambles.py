from random import randint
def generate3x3Scramble(scrambleLength):
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

    return " ".join(scramble)

print(generate3x3Scramble(20))
