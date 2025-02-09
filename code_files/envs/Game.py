import pygame
from code_files.envs.Person import Person


class Game():
    def __init__(self):
        reset = True
        while reset:
            pygame.init()

            #intitialization
            self.screen = pygame.display.set_mode((320,320))
            pygame.display.set_caption("Adam Tries His Best")
            clock = pygame.time.Clock()
            running = True
            self.person_img = pygame.image.load("./person.png").convert()
            self.tree_img = pygame.image.load("./tree.png").convert()
            self.fruit_img = pygame.image.load("./fruit.png").convert()
            self.water_img = pygame.image.load("./water.png").convert()
            self.house_img = pygame.image.load("./house.png").convert()

            #a list of points I randomly generated for the food
            #I divided the 320x320 into 80x80 blocks and selected randomly from inside each one
            self.fruit_pos = [(20,46),(40,133),(62,233),(12,314),(138,63),(132,102),(97,166),(106,247),(205,69),(204,156),(224,194),(232,272),(306,29),(240,101),(242,217),(302,308)]

            #same for water and trees but I wanted one in each quadrant
            #slightly adjusted to prevent overlap
            water_pos=[(107,79),(148,276),(216,18),(172,195)]
            tree_pos=[(19,10),(111,300),(258,105),(195,275)]
            self.house_pos=[]

            #creates the hitboxes to check collisions
            self.hitboxes = []
            for pos in self.fruit_pos:
                box = pygame.Rect(pos[0], pos[1], 16, 16)
                self.hitboxes.append((box, "food")) #(hitbox, type of item)
            for pos in water_pos:
                box = pygame.Rect(pos[0], pos[1], 16, 16)
                self.hitboxes.append((box, "water")) #(hitbox, type of item)
            for pos in tree_pos:
                box = pygame.Rect(pos[0], pos[1], 16, 16)
                self.hitboxes.append((box, "tree")) #(hitbox, type of item)

            x = 0
            y = 0
            score = 0
            self.adam = Person(self.person_img, x, y)
            self.delta_time = .1
            self.can_build = True
            font = pygame.font.Font(None, size = 30)
            #structure from pygame documentation
            while running:
                self.screen.fill((255,255,255))
                score += 1 * self.delta_time
                self.adam.water -= .5 * self.delta_time
                self.adam.food -= .5 * self.delta_time
                self.adam.shelter -= .5 * self.delta_time
                if self.adam.food < 0 or self.adam.water < 0 or self.adam.shelter < 0:
                    running = False

                prompt = f"Food: {self.adam.food:.1f}. Water: {self.adam.water:.1f}\n Wood: {self.adam.wood}, Shelter: {self.adam.shelter}"
                text = font.render(prompt, True, (0,0,0))
                self.screen.blit(text, (0,0))

                # poll for events
                # pygame.QUIT event means the user clicked X to close your window
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        reset=False
                        running = False
                    
                self.hitbox = pygame.Rect(self.adam.x, self.adam.y, 16, 16)
                for i in self.hitboxes:
                    if self.hitbox.colliderect(i[0]):
                        if i[1] == "food":
                            self.adam.food = 60
                            #food can only be used once
                            position = (i[0].left, i[0].top)
                            self.fruit_pos.remove(position)
                            self.hitboxes.remove(i)
                        if i[1] == "water":
                            self.adam.water = 20
                        if i[1] == "tree":
                            self.adam.wood = 1
                        if i[1] == "house":
                            self.adam.shelter = 10
                        self.can_build = False
                    else:
                        self.can_build = True



                clock.tick(60)
                self.delta_time = clock.tick(60) / 1000
                self.delta_time= max(.001, min(.1, self.delta_time))

            pygame.quit()
    def action(self, action):
        if action == 0:
            if self.adam.x > 0: 
                self.adam.x -= 50 * self.delta_time
        if action == 1:
            if self.adam.x < 304: 
                self.adam.x += 50 * self.delta_time
        if action == 2:
            if self.adam.y > 0:  
                self.adam.y -= 50 * self.delta_time
        if action == 3:
            if self.adam.y < 304:  
                self.adam.y += 50 * self.delta_time
        if action == 4:
            if self.can_build and self.adam.wood == 1:
                self.adam.wood = 0
                self.house_pos.append((self.adam.x,self.adam.y))
                box = pygame.Rect(self.adam.x, self.adam.y, 16, 16)
                self.hitboxes.append((box, "house")) #(hitbox, type of item)
    def observe(self):
        return (self.adam.x, self.adam.y, self.adam.food, self.adam.water, self.adam.shelter)
    def evaluate(self):
        for i in self.hitboxes:
            if self.hitbox.colliderect(i[0]):
                if i[1] == "food":
                    return 5
                if i[1] == "water":
                    return 2
                if i[1] == "tree":
                    return 1
                if i[1] == "house":
                    return 2
            else:
                return 0 
    def view(self):
        # RENDER YOUR GAME HERE
                #places fruit, water, and trees
                self.screen.fill((255,255,255))
                for pos in self.fruit_pos:
                    self.screen.blit(self.fruit_img, pos)
                for pos in self.water_pos:
                    self.screen.blit(self.water_img, pos)
                for pos in self.tree_pos:
                    self.screen.blit(self.tree_img, pos)
                for pos in self.house_pos:
                    self.screen.blit(self.house_img, pos)

                self.screen.blit(self.adam.image, (self.adam.x,self.adam.y))
                    
                # flip() the display to put your work on screen
                pygame.display.flip()