import pygame
import pygame.freetype
import json

from Player import Player
from Obstacles import Obstacles as obs
from Constants import *


class Windows:
    def __init__(self, icon, back, progress):
        py_image = pygame.image.load(icon)

        pygame.display.set_icon(py_image)
        pygame.display.set_caption("Club Game" )
        self.screen = pygame.display.set_mode((900, 600))

        self.clock = pygame.time.Clock()
        self.player = Player()

        self.scrolling = 0
        self.hScrolling = 0
        self.pos = 0
        self.levelNum = 1

        self.move = False
        self.drag = False

        self.mousePos1 = (0, 0)
        self.rectangles = []
        self.rectangle = [0, 0, 0, 0]
        self.i = 0

        self.backImage = back

        self.progressPath = progress

        with open(self.progressPath, "r+") as file:
            self.stats = json.load(file)

    def mainMenu(self):
        self.clock.tick(60)

        self.screen.fill(BG)

        startButton = self.createButton((350, 100), (200, 100), 100, "Start", (370, 120), RED, DARK_RED)
        levelsButton = self.createButton((350, 250), (200, 75), 75, "Levels", (365, 265), RED, DARK_RED)
        levelMakerButton = self.createButton((275, 375), (350, 75), 75, "Level Maker", (300, 385), RED, DARK_RED)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "QUIT"
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mousePos = event.pos
                if startButton.collidepoint(mousePos):
                    return "start"
                elif levelsButton.collidepoint(mousePos):
                    return "levels"
                elif levelMakerButton.collidepoint(mousePos):
                    return "levelMaker"
        
        pygame.display.update()

        return "mainMenu"        

    def level(self):
        
        self.clock.tick(60)

        self.screen.fill((173, 216, 230))

        finishLine = obs.finish_line(obs, self.pos, self.screen)

        funcName = f"level{self.levelNum}obstacles"

        obstacles = getattr(obs, funcName)(obs, self.pos, self.screen)

        self.player.display(self.screen)

        finished = self.player.checkCollision(finishLine)
        failed = self.player.checkCollision(obstacles)

        backButton = self.createImageButton(self.backImage, (25, 25), (78, 48))

        percentFinished = round(((self.player.x - 50 + self.pos)/32.5), 1)

        if finished:
            percentFinished = 100
        font = pygame.font.SysFont("None", 50)
        label = font.render(f"Level {self.levelNum}     {percentFinished}%", False, (0, 0, 0))
        self.screen.blit(label, (130, 30))

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
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mousePos = event.pos 
                if backButton.collidepoint(mousePos):
                    self.reset()
                    self.player.reset()
                    return "mainMenu"
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
                    self.updateProgress(self.levelNum)
                    self.reset()
                    self.player.reset()
                    if self.levelNum < 9:
                        self.levelNum += 1
                    return "level"

        return "level"

    def levelMaker(self):
        self.clock.tick(60)
        self.screen.fill((173, 216, 230))

        self.horizontalScroll(0, 2500)
        finishLine = obs.finish_line(obs, self.hScrolling, self.screen)

        character = pygame.draw.rect(self.screen, RED, (50 - self.hScrolling, 300, 30, 30))
        backButton = self.createImageButton(self.backImage, (25, 25), (78, 48))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "QUIT"
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mousePos = event.pos 
                if backButton.collidepoint(mousePos):
                    with open("data/testing.txt", "w") as file:
                        for rect in self.rectangles:
                            file.write(f"rect(window, RED, ({rect[0]} - obstacle_x_change, {rect[1]}, {rect[2]}, {rect[3]}), border_radius=5)\n")

                    return "mainMenu"
                else:
                    self.drag = True
                    self.mousePos1 = event.pos
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                self.drag = False
                r = pygame.rect.Rect(self.rectangle[0] - self.hScrolling, self.rectangle[1], self.rectangle[2], self.rectangle[3])
                if not r.colliderect(character) and r.collidelist(finishLine) == -1:
                    r = pygame.rect.Rect(self.rectangle[0], self.rectangle[1], self.rectangle[2], self.rectangle[3])
                    self.rectangles.append(r)
                else:
                    self.rectangle = [0 - self.hScrolling, 0, 0, 0]
            elif event.type == pygame.MOUSEMOTION and self.drag:                    
                mousePos = event.pos
                self.rectangle[0] = self.mousePos1[0] + self.hScrolling
                self.rectangle[1] = self.mousePos1[1]
                self.rectangle[2] = mousePos[0] - self.mousePos1[0]
                self.rectangle[3] = mousePos[1] - self.mousePos1[1]


        self.rectangle[0] -= self.hScrolling

        r = pygame.rect.Rect(self.rectangle)

        if r.colliderect(character) or r.collidelist(finishLine) != -1:
            pygame.draw.rect(self.screen, RED, self.rectangle)
        elif self.drag:
            pygame.draw.rect(self.screen, GREEN, self.rectangle)

        self.rectangle[0] += self.hScrolling

        for rect in self.rectangles:
            rect.x -= self.hScrolling
            pygame.draw.rect(self.screen, RED, rect)
            rect.x += self.hScrolling

        return "levelMaker"

    def levels(self):
        self.clock.tick(60)
        self.screen.fill((173, 216, 230))

        level1 = self.createButton((50, 100), (200, 100), 75, "Level 1", (65, 125), RED, DARK_RED, self.scrolling)
        level2 = self.createButton((350, 100), (200, 100), 75, "Level 2", (365, 125), RED, DARK_RED, self.scrolling)
        level3 = self.createButton((650, 100), (200, 100), 75, "Level 3", (665, 125), RED, DARK_RED, self.scrolling)
        level4 = self.createButton((50, 250), (200, 100), 75, "Level 4", (65, 275), RED, DARK_RED, self.scrolling)
        level5 = self.createButton((350, 250), (200, 100), 75, "Level 5", (365, 275), RED, DARK_RED, self.scrolling)
        level6 = self.createButton((650, 250), (200, 100), 75, "Level 6", (665, 275), RED, DARK_RED, self.scrolling)
        level7 = self.createButton((50, 400), (200, 100), 75, "Level 7", (65, 425), RED, DARK_RED, self.scrolling)
        level8 = self.createButton((350, 400), (200, 100), 75, "Level 8", (365, 425), RED, DARK_RED, self.scrolling)
        level9 = self.createButton((650, 400), (200, 100), 75, "Level 9", (665, 425), RED, DARK_RED, self.scrolling)
        backButton = self.createImageButton(self.backImage, (25, 25), (78, 48))

        buttonsList = [level1, level2, level3, level4, level5, level6, level7, level8, level9]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "QUIT"
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mousePos = event.pos

                self.scroll(event.button, 0, 225)

                if backButton.collidepoint(mousePos):
                    return "mainMenu"
                
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

        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and self.hScrolling > min:
            self.hScrolling -= 20
        elif (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and self.hScrolling < max:
            self.hScrolling += 20

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

    def createImageButton(self, image, coordinates, dimensions, scrolling=0):
        img = pygame.image.load(image)
        img = pygame.transform.scale(img, dimensions)

        img = self.screen.blit(img, (coordinates[0] + scrolling, coordinates[1] + scrolling))

        return img

    def determineLevel(self): 
        for level in self.stats:
            if not level["beat"]:
                return level["level"]
        
        return level["level"]

    def updateProgress(self, levelNum):
        self.stats[levelNum - 1]["beat"] = True

        with open(self.progressPath, "r+") as file:
            file.seek(0)
            json.dump(self.stats, file, indent=4)
            file.truncate()