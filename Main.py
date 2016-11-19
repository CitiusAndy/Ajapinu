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
appDisplay.blit(textPicture, (350, 250))


pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break

pygame.quit()
    
