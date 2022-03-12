from pygame.draw import rect
from Constants import *

class Obstacles:
    def finish_line(self, obstacle_x_change, window):
        end1 = rect(window, WHITE, (3300 - obstacle_x_change, 0, 50, 50))
        end2 = rect(window, BLACK, (3350 - obstacle_x_change, 0, 50, 50))
        end3 = rect(window, WHITE, (3400 - obstacle_x_change, 0, 50, 50))
        end4 = rect(window, BLACK, (3300 - obstacle_x_change, 50, 50, 50))
        end5 = rect(window, WHITE, (3350 - obstacle_x_change, 50, 50, 50))
        end6 = rect(window, BLACK, (3400 - obstacle_x_change, 50, 50, 50))
        end7 = rect(window, WHITE, (3300 - obstacle_x_change, 100, 50, 50))
        end8 = rect(window, BLACK, (3350 - obstacle_x_change, 100, 50, 50))
        end9 = rect(window, WHITE, (3400 - obstacle_x_change, 100, 50, 50))
        end10 = rect(window, BLACK, (3300 - obstacle_x_change, 150, 50, 50))
        end12 = rect(window, WHITE, (3350 - obstacle_x_change, 150, 50, 50))
        end13 = rect(window, BLACK, (3400 - obstacle_x_change, 150, 50, 50))
        end14 = rect(window, WHITE, (3300 - obstacle_x_change, 200, 50, 50))
        end15 = rect(window, BLACK, (3350 - obstacle_x_change, 200, 50, 50))
        end16 = rect(window, WHITE, (3400 - obstacle_x_change, 200, 50, 50))
        end17 = rect(window, BLACK, (3300 - obstacle_x_change, 250, 50, 50))
        end18 = rect(window, WHITE, (3350 - obstacle_x_change, 250, 50, 50))
        end19 = rect(window, BLACK, (3400 - obstacle_x_change, 250, 50, 50))
        end20 = rect(window, WHITE, (3300 - obstacle_x_change, 300, 50, 50))
        end21 = rect(window, BLACK, (3350 - obstacle_x_change, 300, 50, 50))
        end23 = rect(window, WHITE, (3400 - obstacle_x_change, 300, 50, 50))
        end24 = rect(window, BLACK, (3300 - obstacle_x_change, 350, 50, 50))
        end25 = rect(window, WHITE, (3350 - obstacle_x_change, 350, 50, 50))
        end26 = rect(window, BLACK, (3400 - obstacle_x_change, 350, 50, 50))
        end27 = rect(window, WHITE, (3300 - obstacle_x_change, 400, 50, 50))
        end28 = rect(window, BLACK, (3350 - obstacle_x_change, 400, 50, 50))
        end29 = rect(window, WHITE, (3400 - obstacle_x_change, 400, 50, 50))
        end30 = rect(window, BLACK, (3300 - obstacle_x_change, 450, 50, 50))
        end31 = rect(window, WHITE, (3350 - obstacle_x_change, 450, 50, 50))
        end32 = rect(window, BLACK, (3400 - obstacle_x_change, 450, 50, 50))
        end33 = rect(window, WHITE, (3300 - obstacle_x_change, 500, 50, 50))
        end34 = rect(window, BLACK, (3350 - obstacle_x_change, 500, 50, 50))
        end35 = rect(window, WHITE, (3400 - obstacle_x_change, 500, 50, 50))
        end36 = rect(window, BLACK, (3300 - obstacle_x_change, 550, 50, 50))
        end37 = rect(window, WHITE, (3350 - obstacle_x_change, 550, 50, 50))
        end38 = rect(window, BLACK, (3400 - obstacle_x_change, 550, 50, 50))

        rectList = [end1, end2, end3, end4, end5, end6, end7, end8, end9, end10, end12, end13, end14, end15, end16, end17,
                    end18, end19, end20, end21, end23, end24, end25, end26, end27, end28, end29, end30, end31, end32,
                    end33, end34, end35, end36, end37, end38]

        return rectList

    def level1obstacles(self, obstacle_x_change, window):
        rect1 = rect(window, RED, (0 - obstacle_x_change, 450, 150, 150), border_radius=5)
        rect2 = rect(window, RED, (300 - obstacle_x_change, 500, 150, 100), border_radius=5)
        rect3 = rect(window, RED, (450 - obstacle_x_change, 350, 300, 250), border_radius=5)
        rect4 = rect(window, RED, (800 - obstacle_x_change, 500, 150, 100), border_radius=5)
        rect5 = rect(window, RED, (0 - obstacle_x_change, 0, 150, 150), border_radius=5)
        rect6 = rect(window, RED, (300 - obstacle_x_change, 0, 150, 150), border_radius=5)
        rect7 = rect(window, RED, (450 - obstacle_x_change, 0, 150, 150), border_radius=5)
        rect8 = rect(window, RED, (800 - obstacle_x_change, 0, 150, 150), border_radius=5)
        rect9 = rect(window, RED, (950 - obstacle_x_change, 400, 200, 200), border_radius=5)
        rect10 = rect(window, RED, (950 - obstacle_x_change, 0, 150, 150), border_radius=5)
        rect11 = rect(window, RED, (1100 - obstacle_x_change, 250, 150, 350), border_radius=5)
        rect12 = rect(window, RED, (1100 - obstacle_x_change, 0, 150, 100), border_radius=5)
        rect13 = rect(window, RED, (1500 - obstacle_x_change, 0, 200, 400), border_radius=5)
        rect14 = rect(window, RED, (1500 - obstacle_x_change, 525, 200, 75), border_radius=5)
        rect15 = rect(window, RED, (1700 - obstacle_x_change, 525, 100, 75), border_radius=5)
        rect16 = rect(window, RED, (1700 - obstacle_x_change, 0, 100, 200), border_radius=5)
        rect17 = rect(window, RED, (1800 - obstacle_x_change, 300, 150, 300), border_radius=5)
        rect18 = rect(window, RED, (1800 - obstacle_x_change, 0, 150, 150), border_radius=5)
        rect19 = rect(window, RED, (1950 - obstacle_x_change, 400, 200, 100), border_radius=5)
        rect20 = rect(window, RED, (1950 - obstacle_x_change, 0, 200, 100), border_radius=5)
        rect21 = rect(window, RED, (2250 - obstacle_x_change, 300, 150, 100), border_radius=5)
        rect22 = rect(window, RED, (2250 - obstacle_x_change, 0, 150, 150), border_radius=5)
        rect24 = rect(window, RED, (2500 - obstacle_x_change, 300, 150, 300), border_radius=5)
        rect25 = rect(window, RED, (2650 - obstacle_x_change, 500, 150, 100), border_radius=5)
        rect26 = rect(window, RED, (2800 - obstacle_x_change, 0, 100, 200), border_radius=5)

        rectList = [rect1, rect2, rect3, rect4, rect5, rect6, rect7, rect8, rect9, rect10, rect11, rect12, rect13,
                    rect14, rect15, rect16, rect17, rect18, rect19, rect20, rect21, rect22, rect24, rect25, rect26]

        return rectList

    def level2obstacles(self, obstacle_x_change, window):
        rect1 = rect(window, RED, (0 - obstacle_x_change, 0, 200, 150))
        rect2 = rect(window, RED, (0 - obstacle_x_change, 450, 200, 150))
        rect3 = rect(window, RED, (200 - obstacle_x_change, 0, 150, 300))
        rect4 = rect(window, RED, (350 - obstacle_x_change, 0, 200, 150))
        rect5 = rect(window, RED, (200 - obstacle_x_change, 450, 400, 150))
        rect6 = rect(window, RED, (550 - obstacle_x_change, 0, 200, 50))
        rect7 = rect(window, RED, (550 - obstacle_x_change, 300, 200, 300))
        rect8 = rect(window, RED, (750 - obstacle_x_change, 0, 300, 50))
        rect9 = rect(window, RED, (750 - obstacle_x_change, 175, 300, 425))
        rect10 = rect(window, RED, (1050 - obstacle_x_change, 0, 100, 50))
        rect11 = rect(window, RED, (1050 - obstacle_x_change, 550, 100, 50))
        rect12 = rect(window, RED, (1150 - obstacle_x_change, 0, 300, 400))
        rect13 = rect(window, RED, (1150 - obstacle_x_change, 550, 300, 50))
        rect14 = rect(window, RED, (1450 - obstacle_x_change, 0, 850, 50))
        rect15 = rect(window, RED, (1450 - obstacle_x_change, 550, 850, 50))
        rect16 = rect(window, RED, (1600 - obstacle_x_change, 200, 150, 200))
        rect17 = rect(window, RED, (1900 - obstacle_x_change, 0, 200, 225))
        rect18 = rect(window, RED, (1900 - obstacle_x_change, 375, 200, 225))
        rect19 = rect(window, RED, (2200 - obstacle_x_change, 375, 200, 225))
        rect20 = rect(window, RED, (1900 - obstacle_x_change, 375, 200, 225))
        rect21 = rect(window, RED, (1900 - obstacle_x_change, 375, 200, 225))
        rect22 = rect(window, RED, (1900 - obstacle_x_change, 375, 200, 225))
        rect23 = rect(window, RED, (1900 - obstacle_x_change, 375, 200, 225))
        rect24 = rect(window, RED, (1900 - obstacle_x_change, 375, 200, 225))
        rect25 = rect(window, RED, (1900 - obstacle_x_change, 375, 200, 225))
        rect26 = rect(window, RED, (1900 - obstacle_x_change, 375, 200, 225))

        rectList = [rect1, rect2, rect3, rect4, rect5, rect6, rect7, rect8, rect9, rect10, rect11, rect12, rect13, rect14,
                    rect15, rect16, rect17, rect18, rect19, rect20, rect21, rect22, rect23, rect24, rect25, rect26]

        return rectList

    def level3obstacles(self, obstacle_x_change, window):

        rectList = []

        return rectList

    def level4obstacles(self, obstacle_x_change, window):

        rectList = []

        return rectList

    def level5obstacles(self, obstacle_x_change, window):

        rectList = []

        return rectList

    def level6obstacles(self, obstacle_x_change, window):

        rectList = []

        return rectList

    def level7obstacles(self, obstacle_x_change, window):

        rectList = []

        return rectList

    def level8obstacles(self, obstacle_x_change, window):

        rectList = []

        return rectList

    def level9obstacles(self, obstacle_x_change, window):

        rectList = []

        return rectList
