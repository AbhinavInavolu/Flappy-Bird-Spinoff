import pygame


pygame.init()


def finish_line(obstacle_x_change, window):
    end1 = pygame.draw.rect(window, (255, 255, 255), (3300 - obstacle_x_change, 0, 50, 50))
    end2 = pygame.draw.rect(window, (0, 0, 0), (3350 - obstacle_x_change, 0, 50, 50))
    end3 = pygame.draw.rect(window, (255, 255, 255), (3400 - obstacle_x_change, 0, 50, 50))
    end4 = pygame.draw.rect(window, (0, 0, 0), (3300 - obstacle_x_change, 50, 50, 50))
    end5 = pygame.draw.rect(window, (255, 255, 255), (3350 - obstacle_x_change, 50, 50, 50))
    end6 = pygame.draw.rect(window, (0, 0, 0), (3400 - obstacle_x_change, 50, 50, 50))
    end7 = pygame.draw.rect(window, (255, 255, 255), (3300 - obstacle_x_change, 100, 50, 50))
    end8 = pygame.draw.rect(window, (0, 0, 0), (3350 - obstacle_x_change, 100, 50, 50))
    end9 = pygame.draw.rect(window, (255, 255, 255), (3400 - obstacle_x_change, 100, 50, 50))
    end10 = pygame.draw.rect(window, (0, 0, 0), (3300 - obstacle_x_change, 150, 50, 50))
    end12 = pygame.draw.rect(window, (255, 255, 255), (3350 - obstacle_x_change, 150, 50, 50))
    end13 = pygame.draw.rect(window, (0, 0, 0), (3400 - obstacle_x_change, 150, 50, 50))
    end14 = pygame.draw.rect(window, (255, 255, 255), (3300 - obstacle_x_change, 200, 50, 50))
    end15 = pygame.draw.rect(window, (0, 0, 0), (3350 - obstacle_x_change, 200, 50, 50))
    end16 = pygame.draw.rect(window, (255, 255, 255), (3400 - obstacle_x_change, 200, 50, 50))
    end17 = pygame.draw.rect(window, (0, 0, 0), (3300 - obstacle_x_change, 250, 50, 50))
    end18 = pygame.draw.rect(window, (255, 255, 255), (3350 - obstacle_x_change, 250, 50, 50))
    end19 = pygame.draw.rect(window, (0, 0, 0), (3400 - obstacle_x_change, 250, 50, 50))
    end20 = pygame.draw.rect(window, (255, 255, 255), (3300 - obstacle_x_change, 300, 50, 50))
    end21 = pygame.draw.rect(window, (0, 0, 0), (3350 - obstacle_x_change, 300, 50, 50))
    end23 = pygame.draw.rect(window, (255, 255, 255), (3400 - obstacle_x_change, 300, 50, 50))
    end24 = pygame.draw.rect(window, (0, 0, 0), (3300 - obstacle_x_change, 350, 50, 50))
    end25 = pygame.draw.rect(window, (255, 255, 255), (3350 - obstacle_x_change, 350, 50, 50))
    end26 = pygame.draw.rect(window, (0, 0, 0), (3400 - obstacle_x_change, 350, 50, 50))
    end27 = pygame.draw.rect(window, (255, 255, 255), (3300 - obstacle_x_change, 400, 50, 50))
    end28 = pygame.draw.rect(window, (0, 0, 0), (3350 - obstacle_x_change, 400, 50, 50))
    end29 = pygame.draw.rect(window, (255, 255, 255), (3400 - obstacle_x_change, 400, 50, 50))
    end30 = pygame.draw.rect(window, (0, 0, 0), (3300 - obstacle_x_change, 450, 50, 50))
    end31 = pygame.draw.rect(window, (255, 255, 255), (3350 - obstacle_x_change, 450, 50, 50))
    end32 = pygame.draw.rect(window, (0, 0, 0), (3400 - obstacle_x_change, 450, 50, 50))
    end33 = pygame.draw.rect(window, (255, 255, 255), (3300 - obstacle_x_change, 500, 50, 50))
    end34 = pygame.draw.rect(window, (0, 0, 0), (3350 - obstacle_x_change, 500, 50, 50))
    end35 = pygame.draw.rect(window, (255, 255, 255), (3400 - obstacle_x_change, 500, 50, 50))
    end36 = pygame.draw.rect(window, (0, 0, 0), (3300 - obstacle_x_change, 550, 50, 50))
    end37 = pygame.draw.rect(window, (255, 255, 255), (3350 - obstacle_x_change, 550, 50, 50))
    end38 = pygame.draw.rect(window, (0, 0, 0), (3400 - obstacle_x_change, 550, 50, 50))

    rectlist2 = [end1, end2, end3, end4, end5, end6, end7, end8, end9, end10, end12, end13, end14, end15, end16, end17,
                 end18, end19, end20, end21, end23, end24, end25, end26, end27, end28, end29, end30, end31, end32,
                 end33, end34, end35, end36, end37, end38]

    return rectlist2


def level1obstacles(obstacle_x_change, window):
    rect1 = pygame.draw.rect(window, (255, 0, 0), (0 - obstacle_x_change, 450, 150, 150))
    rect2 = pygame.draw.rect(window, (255, 0, 0), (300 - obstacle_x_change, 500, 150, 100))
    rect3 = pygame.draw.rect(window, (255, 0, 0), (450 - obstacle_x_change, 350, 300, 250))
    rect4 = pygame.draw.rect(window, (255, 0, 0), (800 - obstacle_x_change, 500, 150, 100))
    rect5 = pygame.draw.rect(window, (255, 0, 0), (0 - obstacle_x_change, 0, 150, 150))
    rect6 = pygame.draw.rect(window, (255, 0, 0), (300 - obstacle_x_change, 0, 150, 150))
    rect7 = pygame.draw.rect(window, (255, 0, 0), (450 - obstacle_x_change, 0, 150, 150))
    rect8 = pygame.draw.rect(window, (255, 0, 0), (800 - obstacle_x_change, 0, 150, 150))
    rect9 = pygame.draw.rect(window, (255, 0, 0), (950 - obstacle_x_change, 400, 200, 200))
    rect10 = pygame.draw.rect(window, (255, 0, 0), (950 - obstacle_x_change, 0, 150, 150))
    rect11 = pygame.draw.rect(window, (255, 0, 0), (1100 - obstacle_x_change, 250, 150, 350))
    rect12 = pygame.draw.rect(window, (255, 0, 0), (1100 - obstacle_x_change, 0, 150, 100))
    rect13 = pygame.draw.rect(window, (255, 0, 0), (1500 - obstacle_x_change, 0, 200, 400))
    rect14 = pygame.draw.rect(window, (255, 0, 0), (1500 - obstacle_x_change, 525, 200, 75))
    rect15 = pygame.draw.rect(window, (255, 0, 0), (1700 - obstacle_x_change, 525, 100, 75))
    rect16 = pygame.draw.rect(window, (255, 0, 0), (1700 - obstacle_x_change, 0, 100, 200))
    rect17 = pygame.draw.rect(window, (255, 0, 0), (1800 - obstacle_x_change, 300, 150, 300))
    rect18 = pygame.draw.rect(window, (255, 0, 0), (1800 - obstacle_x_change, 0, 150, 150))
    rect19 = pygame.draw.rect(window, (255, 0, 0), (1950 - obstacle_x_change, 400, 200, 100))
    rect20 = pygame.draw.rect(window, (255, 0, 0), (1950 - obstacle_x_change, 0, 200, 100))
    rect21 = pygame.draw.rect(window, (255, 0, 0), (2250 - obstacle_x_change, 300, 150, 100))
    rect22 = pygame.draw.rect(window, (255, 0, 0), (2250 - obstacle_x_change, 0, 150, 150))
    rect24 = pygame.draw.rect(window, (255, 0, 0), (2500 - obstacle_x_change, 300, 150, 300))
    rect25 = pygame.draw.rect(window, (255, 0, 0), (2650 - obstacle_x_change, 500, 150, 100))
    rect26 = pygame.draw.rect(window, (255, 0, 0), (2800 - obstacle_x_change, 0, 100, 200))

    rectlist = [rect1, rect2, rect3, rect4, rect5, rect6, rect7, rect8, rect9, rect10, rect11, rect12, rect13,
                rect14, rect15, rect16, rect17, rect18, rect19, rect20, rect21, rect22, rect24, rect25, rect26]

    return rectlist


def level2obstacles(obstacle_x_change, window):
    rect1 = pygame.draw.rect(window, (255, 0, 0), (0 - obstacle_x_change, 0, 200, 150))
    rect2 = pygame.draw.rect(window, (255, 0, 0), (0 - obstacle_x_change, 450, 200, 150))
    rect3 = pygame.draw.rect(window, (255, 0, 0), (200 - obstacle_x_change, 0, 150, 300))
    rect4 = pygame.draw.rect(window, (255, 0, 0), (350 - obstacle_x_change, 0, 200, 150))
    rect5 = pygame.draw.rect(window, (255, 0, 0), (200 - obstacle_x_change, 450, 400, 150))
    rect6 = pygame.draw.rect(window, (255, 0, 0), (550 - obstacle_x_change, 0, 200, 50))
    rect7 = pygame.draw.rect(window, (255, 0, 0), (550 - obstacle_x_change, 300, 200, 300))
    rect8 = pygame.draw.rect(window, (255, 0, 0), (750 - obstacle_x_change, 0, 300, 50))
    rect9 = pygame.draw.rect(window, (255, 0, 0), (750 - obstacle_x_change, 175, 300, 425))
    rect10 = pygame.draw.rect(window, (255, 0, 0), (1050 - obstacle_x_change, 0, 100, 50))
    rect11 = pygame.draw.rect(window, (255, 0, 0), (1050 - obstacle_x_change, 550, 100, 50))
    rect12 = pygame.draw.rect(window, (255, 0, 0), (1150 - obstacle_x_change, 0, 300, 400))
    rect13 = pygame.draw.rect(window, (255, 0, 0), (1150 - obstacle_x_change, 550, 300, 50))
    rect14 = pygame.draw.rect(window, (255, 0, 0), (1450 - obstacle_x_change, 0, 850, 50))
    rect15 = pygame.draw.rect(window, (255, 0, 0), (1450 - obstacle_x_change, 550, 850, 50))
    rect16 = pygame.draw.rect(window, (255, 0, 0), (1600 - obstacle_x_change, 200, 150, 200))
    rect17 = pygame.draw.rect(window, (255, 0, 0), (1900 - obstacle_x_change, 0, 200, 225))
    rect18 = pygame.draw.rect(window, (255, 0, 0), (1900 - obstacle_x_change, 375, 200, 225))
    rect19 = pygame.draw.rect(window, (255, 0, 0), (2200 - obstacle_x_change, 375, 200, 225))
    rect20 = pygame.draw.rect(window, (255, 0, 0), (1900 - obstacle_x_change, 375, 200, 225))
    rect21 = pygame.draw.rect(window, (255, 0, 0), (1900 - obstacle_x_change, 375, 200, 225))
    rect22 = pygame.draw.rect(window, (255, 0, 0), (1900 - obstacle_x_change, 375, 200, 225))
    rect23 = pygame.draw.rect(window, (255, 0, 0), (1900 - obstacle_x_change, 375, 200, 225))
    rect24 = pygame.draw.rect(window, (255, 0, 0), (1900 - obstacle_x_change, 375, 200, 225))
    rect25 = pygame.draw.rect(window, (255, 0, 0), (1900 - obstacle_x_change, 375, 200, 225))
    rect26 = pygame.draw.rect(window, (255, 0, 0), (1900 - obstacle_x_change, 375, 200, 225))

    rectlist = [rect1, rect2, rect3, rect4, rect5, rect6, rect7, rect8, rect9, rect10, rect11, rect12, rect13, rect14,
                rect15, rect16, rect17, rect18, rect19, rect20, rect21, rect22, rect23, rect24, rect25, rect26]

    return rectlist
