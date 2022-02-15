import pygame
import obstacles_final as obstacles


class Main:
    def __init__(self):
        pygame.init()

        # Initiating variables
        self.window = pygame.display.set_mode((900, 600))
        self.x, self.y, self.y_velocity, self.obstacle_velocity = [50, 300, 3, 1]
        self.starting_screen, self.main, self.run_level, self.levels_screen = [True, True, True, True]
        self.start_moving, self.moving_up, self.level_ended = [False, False, False]
        self.obstacle_x_change, self.scrolling = [0, 0]
        self.clock = pygame.time.Clock()
        # list of parameters for each level that get passed into the level creation function
        self.levelattrs = [[2, obstacles.level1obstacles, 1], [2, obstacles.level2obstacles, 1],
                           [2, obstacles.level2obstacles, 1], [2, obstacles.level2obstacles, 1],
                           [2, obstacles.level2obstacles, 1], [2, obstacles.level2obstacles, 1],
                           [2, obstacles.level2obstacles, 1], [2, obstacles.level2obstacles, 1],
                           [2, obstacles.level2obstacles, 1]]

        # Display title
        pygame.display.set_caption("Club Game")

# ---------------------------------- Variable Reset Function ------------------------------------------

    def reset(self):
        """resetting variables between different windows like between the
        home screen and the level 1 screen"""
        self.x = 50
        self.y = 300
        self.starting_screen = True
        self.clock = pygame.time.Clock()
        self.main = True
        self.run_level = True
        self.obstacle_x_change = 0
        self.start_moving = False
        self.y_velocity = 3
        self.moving_up = False
        self.obstacle_velocity = 1
        self.levels_screen = True
        self.scrolling = 0
        self.level_ended = False

# --------------------------------------- Main Menu Screen ---------------------------------------

    def main_menu(self):
        """displays the home screen while in the while loop"""
        while self.starting_screen and self.main:

            # Setting FPS
            self.clock.tick(60)

            # Filling window with background color
            self.window.fill((173, 216, 230))

            # Creating start button
            button1 = self.create_button((350, 200), (200, 100), 100, "Start", (370, 220), (255, 0, 0),
                                         (220, 0, 0), self.scrolling)

            # Creating levels button
            button2 = self.create_button((350, 350), (200, 75), 75, "Levels", (365, 365), (255, 0, 0),
                                         (220, 0, 0), self.scrolling)

            # Checking for events
            for event in pygame.event.get():
                # Close if red X is pressed
                if event.type == pygame.QUIT:
                    self.main = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    # Play level 1 when the start button is pressed
                    if button1.collidepoint(mouse_pos[0], mouse_pos[1]):
                        self.starting_screen = False
                        self.reset()
                        self.level(self.levelattrs[0][0], self.levelattrs[0][1], self.levelattrs[0][2])
                    # Open levels screen when levels button is pressed
                    elif button2.collidepoint(mouse_pos[0], mouse_pos[1]):
                        self.starting_screen = False
                        self.reset()
                        self.level_screen()

            # updating display
            pygame.display.update()

# ------------------------------ Player Movement Function ---------------------------------------------

    def movement(self, rectmain, rectlist, player_velocity, obstacle_velocity):
        keys = pygame.key.get_pressed()

        # Character movement
        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and self.start_moving and \
                rectmain.collidelist(rectlist) == -1 and self.level_ended == False and self.x > 0:
            self.x -= player_velocity + obstacle_velocity

        if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and self.start_moving and \
                rectmain.collidelist(rectlist) == -1 and self.level_ended == False and self.x < 870:
            self.x += player_velocity

        if (keys[pygame.K_UP] or keys[pygame.K_w]) and rectmain.collidelist(rectlist) == -1 \
                and self.level_ended == False and self.y > 0:
            # Don't start moving until up or w is pressed
            self.start_moving = True

            # Boolean for if player is moving up so that he moves down if he isn't moving up
            self.moving_up = True

            # Move player up
            self.y -= self.y_velocity

        # Move down if the player isn't moving up and if the level hasn't ended
        if self.moving_up == False and self.start_moving and rectmain.collidelist(rectlist) == -1 \
                and self.level_ended == False and self.y < 570:
            self.y += self.y_velocity

# ---------------------------------- Level Creation Function ---------------------------------------

    def level(self, player_velocity, obstacle_func, obstacle_velocity):
        """Main level creation function"""
        # opens test file and reads some data that gets saved between games like if a level has been beat yet
        while self.main and self.run_level:

            # Setting FPS
            self.clock.tick(60)

            # Filling window with background color
            self.window.fill((173, 216, 230))

            # gets what level is being played by finding what index the
            # parameters are in from the list of level parameters defined during init
            index = self.levelattrs.index([player_velocity, obstacle_func, obstacle_velocity])

            for event in pygame.event.get():
                # Close if red X is pressed
                if event.type == pygame.QUIT:
                    self.main = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    """Events weren't being registered if there were multiple for loops looking for pygame events
                    so everything is packed in one for loop. There is error handling since the buttons that its 
                    checking aren't created until the player has failed or beat the level. """
                    try:
                        if retryButton.collidepoint(mouse_pos[0], mouse_pos[1]) and event.button == 1:
                            self.reset()
                            self.level_ended = False
                            self.level(player_velocity, obstacle_func, obstacle_velocity)
                        elif startscreenButton.collidepoint(mouse_pos[0], mouse_pos[1]) and event.button == 1:
                            self.reset()
                            self.run_level = False
                            self.level_ended = False
                            self.main_menu()
                    except NameError:
                        try:
                            if replayButton.collidepoint(mouse_pos[0], mouse_pos[1]) and event.button == 1:
                                self.reset()
                                self.level_ended = False
                                self.level(player_velocity, obstacle_func, obstacle_velocity)
                            elif startscreenButton2.collidepoint(mouse_pos[0], mouse_pos[1]) and event.button == 1:
                                self.starting_screen = True
                                self.reset()
                                self.level_ended = False
                                self.run_level = False
                                self.main_menu()
                            try:
                                if nextlevelButton.collidepoint(mouse_pos[0], mouse_pos[1]) and event.button == 1:
                                    self.level_ended = False
                                    self.run_level = False
                                    self.reset()
                                    # Change for multiple levels
                                    self.level(self.levelattrs[index + 1][0], self.levelattrs[index + 1][1],
                                               self.levelattrs[index + 1][2])
                            except NameError:
                                pass
                        except NameError:
                            pass

            # Main character
            rectMain = pygame.draw.rect(self.window, (0, 0, 255), (self.x, self.y, 30, 30))

            # Drawing obstacles and making list of obstacles from collision detection
            rectlist = obstacle_func(self.obstacle_x_change, self.window)

            # Drawing finish line and making list of rectangle for collision detection
            rectlist2 = obstacles.finish_line(self.obstacle_x_change, self.window)

            # Player movement
            self.movement(rectMain, rectlist, player_velocity, obstacle_velocity)

            # Display buttons if player failed the level
            if rectMain.collidelist(rectlist) != -1:
                self.level_ended = True
                retryButton = self.create_button((375, 475), (150, 75), 65, "Retry", (390, 490),
                                                 (0, 255, 0), (0, 220, 0))
                startscreenButton = self.create_button((65, 475), (285, 75), 65, "Main Menu", (80, 490),
                                                       (0, 255, 0), (0, 220, 0))

            # Display buttons if player beat the level
            if rectMain.collidelist(rectlist2) != -1:
                self.level_ended = True
                replayButton = self.create_button((375, 475), (175, 75), 65, "Replay", (390, 490),
                                                  (0, 255, 0), (0, 220, 0))
                startscreenButton2 = self.create_button((65, 475), (285, 75), 65, "Main Menu", (80, 490),
                                                        (0, 255, 0), (0, 220, 0))
                if index < len(self.levelattrs) - 1:
                    nextlevelButton = self.create_button((575, 475), (250, 75), 65, "Next Level", (590, 490),
                                                         (0, 255, 0), (0, 220, 0))

            # Reset variable to false so that character moves up only when up or w is pressed
            self.moving_up = False

            # Move all obstacles to left slowly once player has started moving to
            # give the feeling of the player moving forward
            if self.start_moving and self.level_ended == False:
                self.obstacle_x_change += obstacle_velocity

            # Displaying level number and the percent of the level finished
            percent_finished = round(((self.x - 50 + self.obstacle_x_change)/32.5), 1)
            if rectMain.collidelist(rectlist2) != -1:
                percent_finished = 100
            Font = pygame.font.SysFont("None", 50)
            label = Font.render(f"Level {index + 1}       {percent_finished}% Done", False, (0, 0, 0))
            self.window.blit(label, (50, 50))

            pygame.display.update()

# --------------------------- Button Creation Function ----------------------------------------------

    def create_button(self, coordinates, dimensions, fontsize, text, textcooridnates,
                      ac, ic, scrolling=0):
        """Created button based on the parameters passed into it"""
        # Create button
        button = pygame.Rect(coordinates[0], coordinates[1] - scrolling, dimensions[0], dimensions[1])

        # Change button color if mouse is hovering over it
        mouse_pos = pygame.mouse.get_pos()

        if button.collidepoint(mouse_pos[0], mouse_pos[1]):
            pygame.draw.rect(self.window, ic, button)
        else:
            pygame.draw.rect(self.window, ac, button)

        # Add text to button
        Font = pygame.font.SysFont("None", fontsize)
        label = Font.render(text, False, (0, 0, 0))
        self.window.blit(label, (textcooridnates[0], textcooridnates[1] - scrolling))

        return button

# --------------------------- Levels Screen Function ----------------------------------------------------

    def level_screen(self):
        """Level select screen"""
        while self.levels_screen and self.main:
            # Setting FPS
            self.clock.tick(60)

            # Fill window with background color
            self.window.fill((173, 216, 230))

            # Creating level buttons
            button1 = self.create_button((50, 75), (200, 100), 75, "Level 1", (65, 100), (255, 0, 0),
                                         (220, 0, 0), self.scrolling)
            button2 = self.create_button((350, 75), (200, 100), 75, "Level 2", (365, 100), (255, 0, 0),
                                         (220, 0, 0), self.scrolling)
            button3 = self.create_button((650, 75), (200, 100), 75, "Level 3", (665, 100), (255, 0, 0),
                                         (220, 0, 0), self.scrolling)
            button4 = self.create_button((50, 225), (200, 100), 75, "Level 4", (65, 250), (255, 0, 0),
                                         (220, 0, 0), self.scrolling)
            button5 = self.create_button((350, 225), (200, 100), 75, "Level 5", (365, 250), (255, 0, 0),
                                         (220, 0, 0), self.scrolling)
            button6 = self.create_button((650, 225), (200, 100), 75, "Level 6", (665, 250), (255, 0, 0),
                                         (220, 0, 0), self.scrolling)
            button7 = self.create_button((50, 375), (200, 100), 75, "Level 7", (65, 400), (255, 0, 0),
                                         (220, 0, 0), self.scrolling)
            button8 = self.create_button((350, 375), (200, 100), 75, "Level 8", (365, 400), (255, 0, 0),
                                         (220, 0, 0), self.scrolling)
            button9 = self.create_button((650, 375), (200, 100), 75, "Level 9", (665, 400), (255, 0, 0),
                                         (220, 0, 0), self.scrolling)

            buttonsList = [button1, button2, button3, button4, button5, button6, button7, button8, button9]

            # Checking if  button is pressed
            for event in pygame.event.get():

                # Close if red X is pressed
                if event.type == pygame.QUIT:
                    self.main = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos

                    # Scrolling
                    if event.button == 4 and self.scrolling > 0:
                        self.scrolling -= 10
                    elif event.button == 5 and self.scrolling < 200:
                        self.scrolling += 10

                    # Running a level if the corresponding button is pressed
                    for n in buttonsList:
                        location = buttonsList.index(n) + 1
                        if n.collidepoint(mouse_pos[0], mouse_pos[1]) and event.button == 1:
                            self.levels_screen = False
                    # running a level if its corresponding button has been pressed
                    if button1.collidepoint(mouse_pos[0], mouse_pos[1]) \
                            and event.button == 1:
                        self.level(self.levelattrs[0][0], self.levelattrs[0][1], self.levelattrs[0][2])
                    elif button2.collidepoint(mouse_pos[0], mouse_pos[1]) \
                            and event.button == 1:
                        self.level(self.levelattrs[1][0], self.levelattrs[1][1], self.levelattrs[1][2])
                    elif button3.collidepoint(mouse_pos[0], mouse_pos[1]) \
                            and event.button == 1:
                        self.level(self.levelattrs[2][0], self.levelattrs[2][1], self.levelattrs[2][2])
                    elif button4.collidepoint(mouse_pos[0], mouse_pos[1]) \
                            and event.button == 1:
                        self.level(self.levelattrs[3][0], self.levelattrs[3][1], self.levelattrs[3][2])
                    elif button5.collidepoint(mouse_pos[0], mouse_pos[1]) \
                            and event.button == 1:
                        self.level(self.levelattrs[4][0], self.levelattrs[4][1], self.levelattrs[4][2])
                    elif button6.collidepoint(mouse_pos[0], mouse_pos[1]) \
                            and event.button == 1:
                        self.level(self.levelattrs[5][0], self.levelattrs[5][1], self.levelattrs[5][2])
                    elif button7.collidepoint(mouse_pos[0], mouse_pos[1]) \
                            and event.button == 1:
                        self.level(self.levelattrs[6][0], self.levelattrs[6][1], self.levelattrs[6][2])
                    elif button8.collidepoint(mouse_pos[0], mouse_pos[1]) \
                            and event.button == 1:
                        self.level(self.levelattrs[7][0], self.levelattrs[7][1], self.levelattrs[7][2])
                    elif button9.collidepoint(mouse_pos[0], mouse_pos[1]) \
                            and event.button == 1:
                        self.level(self.levelattrs[8][0], self.levelattrs[8][1], self.levelattrs[8][2])

            pygame.display.update()

# ------------------------------------------- Loading Display ----------------------------------------


main = Main()
main.main_menu()

pygame.quit()
