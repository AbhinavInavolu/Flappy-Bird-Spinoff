import  pygame


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
        elif (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and self.move and self.x < 870:
            self.x += 2

        if (keys[pygame.K_UP] or keys[pygame.K_w]) and self.move and self.y > 0:
            self.y -= 3
        elif self.move and self.y < 570:
            self.y += 3
        
        return self.move

    def reset(self):
        self.x = 50
        self.y = 300
        self.move = False