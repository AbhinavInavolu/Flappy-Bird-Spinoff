import json
import pygame

from Windows import Windows

pygame.init()


class Main():
    def __init__(self, icon, progress):
        self.win = Windows(icon)

        self.currentWindow = "mainMenu"
        self.currentLevel = None
        self.run = True
        self.progressPath = progress

        with open(self.progressPath, "r+") as file:
            self.stats = json.load(file)

        self.play()

    def updateProgress(self, levelNum):
        self.stats[levelNum - 1]["beat"] = True

        with open(self.progressPath, "r+") as file:
            file.seek(0)
            json.dump(self.stats, file, indent=4)
            file.truncate()

    def determineLevel(self): 
        for level in self.stats:
            if not level["beat"]:
                return level["level"]
        
        return level["level"]

    def play(self):
        while self.run:
            match self.currentWindow:
                case "mainMenu":
                    self.currentWindow = self.win.mainMenu()
                case "level":
                    self.currentWindow = self.win.level()
                case "start":
                    self.currentLevel = self.determineLevel()
                    self.currentWindow = self.win.level(self.currentLevel)
                case "nextLevel":
                    self.updateProgress(1)
                    self.currentWindow = self.win.level()
                case "levelMaker":
                    self.currentWindow = self.win.levelMaker()
                case "levels":
                    self.currentWindow = self.win.levels()
                case "QUIT":
                    pygame.quit()
                    self.run = False
                    

            pygame.display.update()
