import random
import pygame

class Button():
    def __init__(self, x, y, width, height):
        self.x = x 
        self.y = y 
        self.width = width
        self.height = height

    def clicked(self, pos):
        if self.x < pos[0] < self.x + self.width and self.y < pos[1] < self.y + self.height:
            return True
        return False

class RpsGame():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((960, 640))
        pygame.display.set_caption("RPS Smasher")
        self.bg = pygame.image.load("background.jpg")

        self.r_btn = pygame.image.load("r_button.png").convert_alpha()
        self.p_btn = pygame.image.load("p_button.png").convert_alpha()
        self.s_btn = pygame.image.load("s_button.png").convert_alpha()

        self.choose_rock = pygame.image.load("rock.png").convert_alpha()
        self.choose_paper = pygame.image.load("paper.png").convert_alpha()
        self.choose_scissors = pygame.image.load("scissors.png").convert_alpha()

        self.rock_btn = Button(20, 500, 100, 50)
        self.paper_btn = Button(330, 500, 100, 50)
        self.scissors_btn = Button(640, 500, 100, 50)

        self.pl_score = 0
        self.pc_score = 0
        self.p_option = None
        self.pc_random_choice = None
        self.font = pygame.font.SysFont(None, 48)
        self.text = self.font.render("0 : 0", True, (255, 255, 255))

    def player(self, mouse_pos):
        if self.rock_btn.clicked(mouse_pos):
            self.p_option = "rock"
            self.screen.blit(self.choose_rock, (120, 200))
        elif self.paper_btn.clicked(mouse_pos):
            self.p_option = "paper"
            self.screen.blit(self.choose_paper, (120, 200))
        elif self.scissors_btn.clicked(mouse_pos):
            self.p_option = "scissors"
            self.screen.blit(self.choose_scissors, (120, 200))
        return self.p_option

    def computer(self):
        options = ["rock", "paper", "scissors"]
        pc_choice = random.choice(options)
        if pc_choice == "rock":
            self.pc_random_choice = "rock"
            pc_choice_img = self.choose_rock
        elif pc_choice == "paper":
            self.pc_random_choice = "paper"
            pc_choice_img = self.choose_paper
        else:
            self.pc_random_choice = "scissors"
            pc_choice_img = self.choose_scissors
        self.screen.blit(pc_choice_img, (600, 200))
        return self.pc_random_choice

    def resolve_round(self):
        if self.p_option and self.pc_random_choice:
            if (self.p_option == "rock" and self.pc_random_choice == "scissors") or \
               (self.p_option == "paper" and self.pc_random_choice == "rock") or \
               (self.p_option == "scissors" and self.pc_random_choice == "paper"):
                self.pl_score += 1
            elif self.p_option != self.pc_random_choice:
                self.pc_score += 1
            self.text = self.font.render(f"{self.pl_score} : {self.pc_score}", True, (255, 255, 255))

    def draw_ui(self):
        self.screen.blit(self.bg, (0, 0))
        self.screen.blit(self.r_btn, (20, 500))
        self.screen.blit(self.p_btn, (330, 500))
        self.screen.blit(self.s_btn, (640, 500))
        self.screen.blit(self.text, (330, 0))

    def game_loop(self):
        run = True
        clock = pygame.time.Clock()

        while run:
            self.draw_ui()
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.player(event.pos):
                        self.computer()
                        self.resolve_round()

            clock.tick(30)

        pygame.quit()


if __name__ == '__main__':
    game = RpsGame()
    game.game_loop()
