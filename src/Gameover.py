import pygame 
import time 

pygame.init()

screenwid = (1280)
screenlen = (720)
fscreen = [screenwid, screenlen]

background = pygame.image.load('Castle.jpg')

gameover = pygame.display.set_mode(fscreen)

pygame.display.set_caption("Try again")

gameover.fill("white")

pygame.display.flip()

gameover.blit(background, (0,0))

pygame.display.flip()

pygame.draw.rect(gameover, "black", pygame.Rect(450, 360, 600, 200))
pygame.display.flip()

pygame.time.wait(1000)





