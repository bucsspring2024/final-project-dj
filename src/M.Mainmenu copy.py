import pygame 
import time

pygame.init()

screenwid = (854)
screenlen = (480)

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)


screen = [screenwid, screenlen]
pygame.display.set_caption("Start Menu")

mainmenu = pygame.display.set_mode(screen)

BG = pygame.image.load('assets/blur.png')

MainBG = pygame.transform.scale_by(BG, 0.22)

mainmenu.blit(MainBG, (0,0))

pygame.display.update()

font = pygame.font.Font('freesansbold.ttf', 32)

start = font.render('START', True, green, blue)
quit = font.render('Quit', True, green, blue)


textRect = start.get_rect()
textRect2 = quit.get_rect()

textRect.center = (screenwid// 2, screenlen//2.5)
textRect2.center = (screenwid// 2, screenlen//1.8)

mainmenu.blit(start, textRect)

mainmenu.blit(quit, textRect2 )

pygame.display.update()

pygame.time.wait(10000)

for event in pygame.event.get():


 
        # if event object type is QUIT
        # then quitting the pygame
        # and program both.
        if event.type == pygame.QUIT:
 
            # deactivates the pygame library
            pygame.quit()
 
            # quit the program.
            quit()
 
        # Draws the surface object to the screen.
        pygame.display.update()