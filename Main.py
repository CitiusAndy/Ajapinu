import pygame
from time import time

pygame.init()

displayWidth=1200
displayHeight=800
WHITE=(255,255,255)
BLACK=(0,0,0)

appDisplay=pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption("Ajapinu")
clock=pygame.time.Clock()
appDisplay.fill(WHITE)

def displayTime(text):
    text=str(text)
    timeFont = pygame.font.SysFont("Arial", 72)
    textPicture = timeFont.render(text, False, BLACK, WHITE)
    appDisplay.blit(textPicture, (displayWidth/2-72, displayHeight/2-72))



solveTime="0.00"
displayTime(solveTime)


timerRunning=False
beginTime=0
times=[]
solves=0
appDisplay.fill(WHITE)
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
            times.append(float(solveTime))
    
    displayTime(solveTime)
    pygame.display.update()
    clock.tick(60)


quit()
pygame.quit()
    
