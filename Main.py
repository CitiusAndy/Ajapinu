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

text = "00.00"
timeFont = pygame.font.SysFont("Arial", 72)
textPicture = timeFont.render(text, False, BLACK)
appDisplay.blit(textPicture, (displayWidth/2-72, displayHeight/2-72))

def displayTime(textPicture):
    appDisplay.blit(textPicture, (displayWidth/2-72, displayHeight/2-72))


beginTime=0
timerRunning=False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break
        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_SPACE and not timerRunning:
                print("YES")
                beginTime=time()
                timerRunning=True
            if event.key==pygame.K_SPACE and timerRunning:
                endTime=time()
                timerRunning=False
                
    if beginTime!=0:
        text=str(round(time()-beginTime, 2))
    textPicture=timeFont.render(text, False, BLACK)
    appDisplay.fill(WHITE)
    displayTime(textPicture)
    pygame.display.update()
    clock.tick(60)

pygame.quit()
    
