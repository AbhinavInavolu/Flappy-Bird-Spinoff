import pygame
import json

from Windows import Windows


pygame.init()


class Main():
    def __init__(self, icon, progress):
        self.win = Windows(icon)

        self.currentWindow = "mainMenu"
        self.currentLevel = None

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
        while True:

            self.currentWindow = getattr(Windows, self.currentWindow)(self.win)

            if self.currentWindow == "start":
                self.currentLevel = self.determineLevel()
                self.currentWindow = "level"

            if self.currentWindow == "nextLevel":
                self.updateProgress(1)

            if self.currentWindow == "QUIT":
                pygame.quit()
                break

            pygame.display.update()
