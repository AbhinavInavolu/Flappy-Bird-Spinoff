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