import pygame
import random
import sys
from score import score

class MainMenu:
    """class to handle the main menu interface and interactions."""
    def __init__(self):
        pygame.init()
        self.score = score()
        self.screen = pygame.display.set_mode((854, 480))
        pygame.display.set_caption('Game')
        self.screen_width = 854
        self.screen_height = 480
        self.clock = pygame.time.Clock()

        self.background_color = (128, 128, 128)
        self.button_color = (160, 160, 220)
        self.button_hover_color = (160, 160, 160)
        self.text_color = (255, 255, 255)
        self.MainBG = pygame.image.load('assets/blur.png')
        self.scaleBG = pygame.transform.scale_by(self.MainBG, 0.22)
        self.PlayBG = pygame.image.load('assets/battle.png')
        self.PlayScaleBG = pygame.transform.scale_by(self.PlayBG, 3.35)
        self.enemy = pygame.image.load('assets/Arc.png')
        self.character = pygame.image.load('assets/char.png')
        self.characterS = pygame.transform.scale_by(self.character, 1.8)
        self.enemyS = pygame.transform.scale_by(self.enemy, 1)
        self.hyperEF = pygame.image.load('assets/hyperEF.png')
        self.hyperS= pygame.transform.scale_by(self.hyperEF, 0.2)
        self.fireEF = pygame.image.load('assets/fireEF.png')
        self.fireS = pygame.transform.scale_by(self.fireEF, 0.2)

        self.font = pygame.font.Font(None, 36)
        self.buttons = [
            {"label": "Start Game", "rect": pygame.Rect(self.screen_width / 2 - 100, 225, 200, 50), "action": self.start_game},
            {"label": "Quit", "rect": pygame.Rect(self.screen_width / 2 - 100, 300, 200, 50), "action": self.quit},
        ]
    def attack(self, kwargs={}):
        options = ("rock", "paper", "scissors")

        player = kwargs["label"].lower()
        computer = random.choice(options)
        print(f"player is {player} computer is {computer}")

        if player == computer:
            self.tiescreen()
        elif player == "rock" and computer == "scissors":
            self.winscreen()
        elif player == "paper" and computer == "rock":
            self.winscreen()
        elif player == "scissors" and computer == "paper":
            self.winscreen()
        else:
            self.losescreen()
        

    def winscreen(self):
        running = True
        self.score.win()
        print(self.score.data)
        while running:
            self.buttons = [
                {"label": f"You Win {self.score.data}", "rect": pygame.Rect(self.screen_width / 2 - 2, 300, 400, 50), "action": self.quit},]
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.quit()
                        return
                    elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        if self.handle_button_click(event.pos):
                            return   
  
            self.screen.fill(self.bg_color)
            self.screen.blit(self.PlayScaleBG, (0,0))
            self.draw_buttons() 
     
                
            self.screen.blit(self.enemyS, (500, 30))
            self.screen.blit(self.characterS, (50, 160))
         
            self.screen.blit(self.fireR, (0,0))
            pygame.display.update()
            self.clock.tick(60)
    def losescreen(self, kwargs={}):
        self.score.loss()
        print(self.score.data)
        running = True
        while running:
            self.buttons = [
                {"label": f"You Lose {self.score.data}", "rect": pygame.Rect(self.screen_width / 2 - 2, 300, 400, 50), "action": self.quit},]
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.quit()
                        return
                    elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        if self.handle_button_click(event.pos):
                            return   
   
            self.screen.fill(self.bg_color)
            self.screen.blit(self.PlayScaleBG, (0,0))

            self.draw_buttons() 
          
            self.screen.blit(self.enemyS, (500, 30))
            self.screen.blit(self.characterS, (50, 160))
            self.screen.blit(self.hyperR, (0,0))
            pygame.display.update()
            self.clock.tick(60)
    def tiescreen(self, kwargs={}):
        self.score.tie()
        print(self.score.data)
        running = True
        while running:
            self.buttons = [
                {"label": f"You tied{self.score.data}", "rect": pygame.Rect(self.screen_width / 2 - 2, 300, 400, 50), "action": self.quit},]
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.quit()
                        return
                    elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                        if self.handle_button_click(event.pos):
                            return   
   
            self.screen.fill(self.bg_color)
            self.screen.blit(self.PlayScaleBG, (0,0))

            self.draw_buttons() 
          
            self.screen.blit(self.enemyS, (500, 30))
            self.screen.blit(self.characterS, (50, 160))
            pygame.display.update()
            self.clock.tick(60)
    

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.handle_button_click(event.pos)

            self.screen.fill(self.background_color)
            self.screen.blit(self.scaleBG, (0,0))
            self.draw_buttons()
            pygame.display.flip()
            self.clock.tick(60)

    def draw_buttons(self):
        mouse_pos = pygame.mouse.get_pos()
        for button in self.buttons:
            rect = button['rect']
            color = self.button_hover_color if rect.collidepoint(mouse_pos) else self.button_color
            pygame.draw.rect(self.screen, color, rect)
            text_surf = self.font.render(button['label'], True, self.text_color)
            text_rect = text_surf.get_rect(center=rect.center)
            self.screen.blit(text_surf, text_rect)

    def handle_button_click(self, mouse_pos):
        for button in self.buttons:
            if button['rect'].collidepoint(mouse_pos):
                button['action']({"label": button["label"]})

    def start_game(self, kwargs={}):
        self.main_menu = self.screen
        self.bg_color = (50, 50, 50)
        self.button_color = (225, 0, 0)
        self.button_hover_color = (150, 150, 200)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.Font(None, 36)

        self.buttons = [
            {"label": "Scissors", "rect": pygame.Rect(self.screen_width / 2 - 2, 400, 200, 50), "action": self.attack},
            {"label": "Paper", "rect": pygame.Rect(self.screen_width / 2 - 2, 350, 200, 50), "action": self.attack},
            {"label": "Rock", "rect": pygame.Rect(self.screen_width / 2 - 2, 300, 200, 50), "action": self.attack},
        ]
        
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if self.handle_button_click(event.pos):
                        return

            self.screen.fill(self.bg_color)
            self.screen.blit(self.PlayScaleBG, (0,0))
            self.draw_buttons()
            # pygame.display.flip()
            self.screen.blit(self.enemyS, (500, 30))
            self.screen.blit(self.characterS, (50, 160))
            pygame.display.flip()
            self.clock.tick(60)

    def quit(self, kwargs={}):
        self.score.setscores()
        pygame.quit()
        sys.exit()
    

if __name__ == "__main__":
    pygame.init()
    menu = MainMenu()
    menu.run()
