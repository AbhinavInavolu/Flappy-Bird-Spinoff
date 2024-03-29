import pygame

from Player import Player
from Obstacles import Obstacles as obs
from Constants import *


class Windows:
    def __init__(self, icon):
        py_image = pygame.image.load(icon)

        pygame.display.set_icon(py_image)
        pygame.display.set_caption("Club Game" )
        self.screen = pygame.display.set_mode((900, 600))

        self.clock = pygame.time.Clock()
        self.player = Player()

        self.scrolling = 0
        self.hScrollng = 0
        self.pos = 0
        self.levelNum = 1

        self.move = False
        self.drag = False

        self.mousePos1 = (0, 0)
        self.rectangles = []
        self.rectangle = pygame.rect.Rect(0, 0, 0 ,0)
        self.i = 0

    def mainMenu(self):
        self.clock.tick(60)

        self.screen.fill(BG)

        startButton = self.createButton((350, 100), (200, 100), 100, "Start", (370, 120), RED, DARK_RED)
        levelsButton = self.createButton((350, 250), (200, 75), 75, "Levels", (365, 265), RED, DARK_RED)
        levelMakerButton = self.createButton((275, 375), (350, 75), 75, "Level Maker", (300, 385), RED, DARK_RED)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "QUIT"
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = event.pos
                if startButton.collidepoint(mousePos):
                    return "start"
                elif levelsButton.collidepoint(mousePos):
                    return "levels"
                elif levelMakerButton.collidepoint(mousePos):
                    return "levelMaker"
        
        pygame.display.update()

        return "mainMenu"        

    def level(self, num=False):
        if not num:
            num = self.levelNum
        
        self.clock.tick(60)

        self.screen.fill((173, 216, 230))

        finishLine = obs.finish_line(obs, self.pos, self.screen)

        funcName = f"level{num}obstacles"

        obstacles = getattr(obs, funcName)(obs, self.pos, self.screen)

        self.player.display(self.screen)

        finished = self.player.checkCollision(finishLine)
        failed = self.player.checkCollision(obstacles)

        if not(finished or failed): 
            self.move = self.player.movement()

            if self.move:
                self.pos += 1

        if finished: 
            replayButton = self.createButton((375, 475), (175, 75), 65, "Replay", (390, 490), GREEN, DARK_GREEN)
            mainMenuButton = self.createButton((70, 475), (275, 75), 65, "Main Menu", (90, 490), GREEN, DARK_GREEN)
            nextlevelButton = self.createButton((575, 475), (250, 75), 65, "Next Level", (590, 490), GREEN, DARK_GREEN)

        elif failed: 
            replayButton = self.createButton((375, 475), (145, 75), 65, "Retry", (390, 490), GREEN, DARK_GREEN)
            mainMenuButton = self.createButton((70, 475), (275, 75), 65, "Main Menu", (90, 490), GREEN, DARK_GREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                return "QUIT"
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = event.pos 
                if "mainMenuButton" in locals(): 
                    if replayButton.collidepoint(mousePos):
                        self.reset()
                        self.player.reset()
                        return "level" 
                    elif mainMenuButton.collidepoint(mousePos):
                        self.reset()
                        self.player.reset()
                        return "mainMenu"
                if "nextlevelButton" in locals() and nextlevelButton.collidepoint(mousePos):
                    self.reset()
                    self.player.reset()
                    if self.levelNum < 9:
                        self.levelNum += 1
                    return "level"

        return "level"

    def levelMaker(self):
        self.clock.tick(60)
        self.screen.fill((173, 216, 230))

        self.horizontalScroll(-100, 2500)
        obs.finish_line(obs, self.hScrollng, self.screen)

        character = pygame.draw.rect(self.screen, RED, (50, 300, 30, 30))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "QUIT"
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.drag = True
                    self.mousePos1 = event.pos
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    self.drag = False
                    r = pygame.rect.Rect(self.rectangle.x, self.rectangle.y, self.rectangle.width, self.rectangle.height)
                    if not r.colliderect(character):
                        self.rectangles.append(r)
                    else:
                        self.rectangle = pygame.rect.Rect(0, 0, 0 ,0)
            elif event.type == pygame.MOUSEMOTION and self.drag:                    
                mousePos = event.pos
                self.rectangle.x = self.mousePos1[0] - self.hScrollng
                self.rectangle.y = self.mousePos1[1]
                self.rectangle.width = mousePos[0] - self.mousePos1[0]
                self.rectangle.height = mousePos[1] - self.mousePos1[1]
    
        if self.rectangle.colliderect(character):
            pygame.draw.rect(self.screen, RED, self.rectangle)
        else :
            pygame.draw.rect(self.screen, GREEN, self.rectangle)


        for rect in self.rectangles:
            pygame.draw.rect(self.screen, RED, rect)

        return "levelMaker"

    def levels(self):
        self.clock.tick(60)
        self.screen.fill((173, 216, 230))

        level1 = self.createButton((50, 75), (200, 100), 75, "Level 1", (65, 100), RED, DARK_RED, self.scrolling)
        level2 = self.createButton((350, 75), (200, 100), 75, "Level 2", (365, 100), RED, DARK_RED, self.scrolling)
        level3 = self.createButton((650, 75), (200, 100), 75, "Level 3", (665, 100), RED, DARK_RED, self.scrolling)
        level4 = self.createButton((50, 225), (200, 100), 75, "Level 4", (65, 250), RED, DARK_RED, self.scrolling)
        level5 = self.createButton((350, 225), (200, 100), 75, "Level 5", (365, 250), RED, DARK_RED, self.scrolling)
        level6 = self.createButton((650, 225), (200, 100), 75, "Level 6", (665, 250), RED, DARK_RED, self.scrolling)
        level7 = self.createButton((50, 375), (200, 100), 75, "Level 7", (65, 400), RED, DARK_RED, self.scrolling)
        level8 = self.createButton((350, 375), (200, 100), 75, "Level 8", (365, 400), RED, DARK_RED, self.scrolling)
        level9 = self.createButton((650, 375), (200, 100), 75, "Level 9", (665, 400), RED, DARK_RED, self.scrolling)

        buttonsList = [level1, level2, level3, level4, level5, level6, level7, level8, level9]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "QUIT"
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = event.pos

                self.scroll(event.button, 0, 200)
                
                for i in range(len(buttonsList)):
                    if buttonsList[i].collidepoint(mousePos) and event.button == 1:
                        self.levelNum = i + 1
                        return "level"     

        return "levels"        

    def reset(self):
        self.scrolling = 0
        self.pos = 0
        self.move = False

    def horizontalScroll(self, min, max):
        keys = pygame.key.get_pressed()

        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and self.hScrollng > min:
            self.hScrollng -= 50
        elif (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and self.hScrollng < max:
            self.hScrollng += 50

    def scroll(self, event, min, max):
        if event == 4 and self.scrolling > min:
            self.scrolling -= 10
        elif event == 5 and self.scrolling < max:
            self.scrolling += 10

    def createButton(self, coordinates, dimensions, fontsize, text, textcoordinates, ac, ic, scrolling=0, rad=10):
        button = pygame.Rect(coordinates[0], coordinates[1] - scrolling, dimensions[0], dimensions[1])

        mouse_pos = pygame.mouse.get_pos()

        if button.collidepoint(mouse_pos[0], mouse_pos[1]):
            pygame.draw.rect(self.screen, ic, button, border_radius=rad)
        else:
            pygame.draw.rect(self.screen, ac, button, border_radius=rad)

        font = pygame.font.SysFont("None", fontsize)
        label = font.render(text, False, (0, 0, 0))

        self.screen.blit(label, (textcoordinates[0], textcoordinates[1] - scrolling))

        return button
