import pygame
import ObstaclesTest as obs
import json

pygame.init()


class Player:
    def __init__(self):
        self.x = 50
        self.y = 300
        self.main = None
        self.move = False
    
    def display(self, screen):
        self.main = pygame.draw.rect(screen, (0, 0, 255), (self.x, self.y, 30, 30))

    def checkCollision(self, rectList):
        if self.main.collidelist(rectList) != -1:
            return True

        return False

    def movement(self):
        keys = pygame.key.get_pressed()

        if (keys[pygame.K_LEFT] or keys[pygame.K_a] or
            keys[pygame.K_RIGHT] or keys[pygame.K_d] or 
            keys[pygame.K_UP] or keys[pygame.K_w]):
            self.move = True

        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and self.move and self.x > 0:
            self.x -= 3

        if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and self.move and self.x < 870:
            self.x += 2

        if (keys[pygame.K_UP] or keys[pygame.K_w]) and self.move and self.y > 0:
            self.y -= 6

        if self.move and self.y < 570:
            self.y += 3
        
        return self.move

    def reset(self):
        self.x = 50
        self.y = 300
        self.move = False

class Window:
    def __init__(self):
        self.screen = pygame.display.set_mode((900, 600))
        self.clock = pygame.time.Clock()
        self.scrolling = 0
        self.pos = 0
        self.player = Player()
        self.move = False
    
    def reset(self):
        self.scrolling = 0
        self.pos = 0
        self.move = False

    def mainMenu(self):
        self.clock.tick(60)

        self.screen.fill((173, 216, 230))

        startButton = self.createButton((350, 100), (200, 100), 100, "Start", (370, 120), (255, 0, 0), (220, 0, 0), self.scrolling)
        levelsButton = self.createButton((350, 250), (200, 75), 75, "Levels", (365, 265), (255, 0, 0), (220, 0, 0), self.scrolling)
        levelMakerButton = self.createButton((275, 375), (350, 75), 75, "Level Maker", (300, 385), (255, 0, 0), (220, 0, 0), self.scrolling)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "QUIT"
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = event.pos
                if startButton.collidepoint(mousePos[0], mousePos[1]):
                    return "start"
                elif levelsButton.collidepoint(mousePos[0], mousePos[1]):
                    return "levels"
                elif levelMakerButton.collidepoint(mousePos[0], mousePos[1]):
                    return "levelMaker"
        
        pygame.display.update()

        return "mainMenu"        

    def level(self):
        self.clock.tick(60)

        self.screen.fill((173, 216, 230))

        finishLine = obs.finish_line(self.pos, self.screen)
        obstacles = obs.level1obstacles(self.pos, self.screen)

        self.player.display(self.screen)

        finished = self.player.checkCollision(finishLine)
        failed = self.player.checkCollision(obstacles)

        if not(finished or failed): # stopping movment after either losing or beating the level
            self.move = self.player.movement()

            if self.move:
                self.pos += 1

        if finished: # drawing buttons if you finished the level
            replayButton = self.createButton((375, 475), (175, 75), 65, "Replay", (390, 490), (0, 255, 0), (0, 220, 0))
            mainMenuButton = self.createButton((65, 475), (285, 75), 65, "Main Menu", (80, 490), (0, 255, 0), (0, 220, 0))
            nextlevelButton = self.createButton((575, 475), (250, 75), 65, "Next Level", (590, 490), (0, 255, 0), (0, 220, 0))

        elif failed: # drawing buttons if you failed the level
            replayButton = self.createButton((375, 475), (175, 75), 65, "Retry", (390, 490), (0, 255, 0), (0, 220, 0))
            mainMenuButton = self.createButton((65, 475), (285, 75), 65, "Main Menu", (80, 490), (0, 255, 0), (0, 220, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT: # closing the game
                return "QUIT"
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = event.pos # using locals since these buttons aren't crea
                if "mainMenuButton" in locals(): # checking if you pressed a button
                    if replayButton.collidepoint(mousePos[0], mousePos[1]):
                        self.reset()
                        self.player.reset()
                        return "level" 
                    elif mainMenuButton.collidepoint(mousePos[0], mousePos[1]):
                        self.reset()
                        self.player.reset()
                        return "mainMenu"
                if "nextlevelButton" in locals() and nextlevelButton.collidepoint(mousePos[0], mousePos[1]):
                    self.reset()
                    self.player.reset()
                    return "nextLevel"

        return "level"

    def levelMaker(self):
        self.clock.tick(60)
        self.screen.fill((173, 216, 230))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "QUIT"

        return "levelMaker"

    def levels(self):
        self.clock.tick(60)
        self.screen.fill((173, 216, 230))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "QUIT"

        return "levels"        

    def createButton(self, coordinates, dimensions, fontsize, text, textcooridnates, ac, ic, scrolling=0):
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
        self.currentWindow = "mainMenu"
        self.run = True
        self.currentLevel = None

        with open("Progress.json", "r+") as file:
            self.stats = json.load(file)

    def updateProgress(self, levelNum):
        self.stats[levelNum - 1]["beat"] = True

        with open("Progress.json", "r+") as file:
            file.seek(0)
            json.dump(self.stats, file, indent=4)
            file.truncate()

    def determineLevel(self): # reading json to check which level to start you on
        for level in self.stats:
            if not level["beat"]:
                return level["level"]
        
        return level["level"]

    def play(self):
        while self.run:
            self.currentWindow = getattr(Window, self.currentWindow)(self.win)

            if self.currentWindow == "start":
                self.currentLevel = self.determineLevel()
                self.currentWindow = "level"

            if self.currentWindow == "nextLevel":
                self.updateProgress(1)

            if self.currentWindow == "QUIT":
                pygame.quit()
                self.run = False

            pygame.display.update()

main = Main()
main.play()

# Obstacles.end()