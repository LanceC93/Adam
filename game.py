import pygame

from Person import Person

pygame.init()

#intitialization
screen = pygame.display.set_mode((320,320))
pygame.display.set_caption("Adam Tries His Best")
clock = pygame.time.Clock()
running = True
person_img = pygame.image.load("person.png").convert()
tree_img = pygame.image.load("tree.png").convert()
fruit_img = pygame.image.load("fruit.png").convert()
water_img = pygame.image.load("water.png").convert()
adam = Person(person_img, 120, 120)

#a list of points I randomly generated for the food
#I divided the 320x320 into 80x80 blocks and selected randomly from inside each one
fruit_pos = [(20,46),(40,133),(62,233),(12,314),(138,63),(132,102),(97,166),(106,247),(205,69),(204,156),(224,194),(232,272),(306,29),(240,101),(242,217),(302,308)]

#same for water and trees but I wanted one in each quadrant
#slightly adjusted to prevent overlap
water_pos=[(107,79),(148,276),(216,18),(172,195)]
tree_pos=[(19,119),(111,300),(258,105),(195,275)]

x = 0
y = 0
adam = Person(person_img, x, y)
delta_time = .1
#structure from pygame documentation
while running:
    screen.fill((255,255,255))

    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        if adam.x > 0: 
            adam.x -= 50 * delta_time
    if keys[pygame.K_RIGHT]:
        if adam.x < 304: 
            adam.x += 50 * delta_time
    if keys[pygame.K_UP]:
        if adam.y > 0:  
            adam.y -= 50 * delta_time
    if keys[pygame.K_DOWN]:
        if adam.y < 304:  
            adam.y += 50 * delta_time
    hitbox = pygame.Rect(adam.x, adam.y, 16, 16)


        
    # RENDER YOUR GAME HERE
    #places fruit, water, and trees
    for pos in fruit_pos:
        screen.blit(fruit_img, pos)
    for pos in water_pos:
        screen.blit(water_img, pos)
    for pos in tree_pos:
        screen.blit(tree_img, pos)

    screen.blit(adam.image, (adam.x,adam.y))
        
    # flip() the display to put your work on screen
    pygame.display.flip()

    delta_time = clock.tick(60) / 1000
    delta_time= max(.001, min(.1, delta_time))

pygame.quit()