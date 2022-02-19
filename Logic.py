import pygame
import json

from Window import Window


pygame.init()


class Main(Window):
    def __init__(self):
        self.win = Window()
        self.currentWindow = "mainMenu"
        self.currentLevel = None

        with open("Progress.json", "r+") as file:
            self.stats = json.load(file)

        self.play()

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
        while True:

            self.currentWindow = getattr(Window, self.currentWindow)(self.win)

            if self.currentWindow == "start":
                self.currentLevel = self.determineLevel()
                self.currentWindow = "level"

            if self.currentWindow == "nextLevel":
                self.updateProgress(1)

            if self.currentWindow == "QUIT":
                pygame.quit()
                break

            pygame.display.update()