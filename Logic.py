import pygame

from Windows import Windows


pygame.init()


class Main():
    def __init__(self, icon, progress, back):
        self.win = Windows(icon, back, progress)

        self.currentWindow = "mainMenu"
        self.run = True

        self.play()

    def play(self):
        while self.run:
            match self.currentWindow:
                case "mainMenu":
                    self.currentWindow = self.win.mainMenu()
                case "level":
                    self.currentWindow = self.win.level()
                case "start":
                    self.currentWindow = self.win.level()
                case "nextLevel":
                    self.currentWindow = self.win.level()
                case "levelMaker":
                    self.currentWindow = self.win.levelMaker()
                case "levels":
                    self.currentWindow = self.win.levels()
                case "QUIT":
                    self.run = False
                    

            pygame.display.update()

        pygame.quit()
