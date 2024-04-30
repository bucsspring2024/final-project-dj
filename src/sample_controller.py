import pygame

class Controller:
    """class to control player actions like left, right, jump, and crouch."""
    def __init__(self):
        self.left = False
        self.right = False
        self.jump = False
        self.crouch = False

    def move_left(self):
        self.left = True
    
    def move_right(self):
        self.right = True
        
    def jump_action(self):
        self.jump = True
        
    def crouch_action(self):
        self.crouch = True

class MainMenu:
    """class to handle the main menu interface and interactions."""
    def __init__(self, screen):
        self.screen = screen
        self.screen_width = self.screen.get_width()
        self.screen_height = self.screen.get_height()
        self.clock = pygame.time.Clock()

        self.bg_color = (30, 30, 30)
        self.button_color = (100, 100, 200)
        self.button_hover_color = (150, 150, 250)
        self.text_color = (255, 255, 255)

        self.font = pygame.font.Font(None, 36)
        self.buttons = [
            {"label": "Start Game", "rect": pygame.Rect(self.screen_width / 2 - 100, 150, 200, 50), "action": self.start_game},
            {"label": "Options", "rect": pygame.Rect(self.screen_width / 2 - 100, 250, 200, 50), "action": self.open_options},
        ]

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.handle_button_click(event.pos)

            self.screen.fill(self.bg_color)
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
                button['action']()

    def start_game(self):
        print("Game started!")

    def open_options(self):
        print("Options menu!")

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Main Menu')

    menu = MainMenu(screen)
    menu.run()