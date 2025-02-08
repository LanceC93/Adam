import pygame

pygame.init()

#intitialization
screen = pygame.display.set_mode((320,320))
clock = pygame.time.Clock()
running = True
person_img = pygame.image.load("person.png").convert()
tree_img = pygame.image.load("tree.png").convert()
fruit_img = pygame.image.load("fruit.png").convert()
water_img = pygame.image.load("water.png").convert()

#a list of points I randomly generated for the food
#I divided the 320x320 into 80x80 blocks and selected randomly from inside each one
fruit_pos = [(20,46),(40,133),(62,233),(12,314),(138,63),(132,102),(97,166),(106,247),(205,69),(204,156),(224,194),(232,272),(306,29),(240,101),(242,217),(302,308)]

#same for water and trees but I wanted one in each quadrant
#slightly adjusted to prevent overlap
water_pos=[(107,79),(148,276),(216,18),(172,195)]
tree_pos=[(19,119),(111,300),(258,105),(195,275)]

#places fruit, water, and trees
for pos in fruit_pos:
    screen.blit(fruit_img, pos)
for pos in water_pos:
    screen.blit(water_img, pos)
for pos in tree_pos:
    screen.blit(tree_img, pos)
    

#structure from pygame documentation
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(person_img, (120,120))
        
    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()