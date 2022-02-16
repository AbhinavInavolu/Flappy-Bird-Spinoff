import pygame
import obstacles_test as obstacles


pygame.init()


class Player:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.main
    
    def display(self, screen):
        self.main = pygame.draw.rect(screen, (0, 0, 255), (self.x, self.y, 30, 30))

    def checkCollision(self, rectList):
        if self.main.collidelist(rectList) != -1:
            return True


class Window:
    def __init__(self):
        self.screen = pygame.display.set_mode((900, 600))
        self.clock = pygame.time.Clock()
        self.run = True
        self.scrolling = 0
    
    def mainMenu(self):
        while self.run:
            self.clock.tick(60)

            self.screen.fill((173, 216, 230))

            startButton = self.create_button((350, 200), (200, 100), 100, "Start", (370, 220), (255, 0, 0), (220, 0, 0), self.scrolling)
            levelsButton = self.create_button((350, 350), (200, 75), 75, "Levels", (365, 365), (255, 0, 0), (220, 0, 0), self.scrolling)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "QUIT"
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mousePos = event.pos
                    if startButton.collidepoint(mousePos[0], mousePos[1]):
                        return "start"
                    elif levelsButton.collidepoint(mousePos[0], mousePos[1]):
                        return "levels"
            
            pygame.display.update()


    def create_button(self, coordinates, dimensions, fontsize, text, textcooridnates, ac, ic, scrolling=0):
        button = pygame.Rect(coordinates[0], coordinates[1] - scrolling, dimensions[0], dimensions[1])

        mouse_pos = pygame.mouse.get_pos()

        if button.collidepoint(mouse_pos[0], mouse_pos[1]):
            pygame.draw.rect(self.screen, ic, button)
        else:
            pygame.draw.rect(self.screen, ac, button)

        font = pygame.font.SysFont("None", fontsize)
        label = font.render(text, False, (0, 0, 0))

        self.screen.blit(label, (textcooridnates[0], textcooridnates[1] - scrolling))

        return button


class Main(Window, Player):
    def __init__(self):
        self.win = Window()

    def play(self):
        self.win.mainMenu()


main = Main()
main.play()
