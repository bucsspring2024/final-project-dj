import pygame 

pygame.init()

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

start = font.render('Try again?', True, green, blue)
quit = font.render('Exit Game', True, green, blue)


textRect = start.get_rect()
textRect2 = quit.get_rect()

textRect.center = (screenwid// 2, screenlen//2.5)
textRect2.center = (screenwid// 2, screenlen//1.8)

mainmenu.blit(start, textRect)

mainmenu.blit(quit, textRect2 )

pygame.display.update()

pygame.time.wait(10000)

def menu():
    while True:
        screen.fill("black")

        MENU_POS = pygame.mouse.get_pos() #gets position of mouse

        TEXT = get_font(100).render("START MENU", True, "#b68f40")
        Rect = TEXT.get_rect = (640, 100)

        Start_Game = 

        End_Game = 

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Start_Game.checkForInput(MENU_POS):
                    play()
                if End_Game.checkForInput(MENU_POS):
                    pygame.quit()
        pygame.display.update()
        pass

def game():
    while True:
        screen.fill()
        pass

        

    

