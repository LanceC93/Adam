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
house_img = pygame.image.load("house.png").convert()
adam = Person(person_img, 120, 120)

#a list of points I randomly generated for the food
#I divided the 320x320 into 80x80 blocks and selected randomly from inside each one
fruit_pos = [(20,46),(40,133),(62,233),(12,314),(138,63),(132,102),(97,166),(106,247),(205,69),(204,156),(224,194),(232,272),(306,29),(240,101),(242,217),(302,308)]

#same for water and trees but I wanted one in each quadrant
#slightly adjusted to prevent overlap
water_pos=[(107,79),(148,276),(216,18),(172,195)]
tree_pos=[(19,10),(111,300),(258,105),(195,275)]
house_pos=[]

#creates the hitboxes to check collisions
hitboxes = []
for pos in fruit_pos:
    box = pygame.Rect(pos[0], pos[1], 16, 16)
    hitboxes.append((box, "food")) #(hitbox, type of item)
for pos in water_pos:
    box = pygame.Rect(pos[0], pos[1], 16, 16)
    hitboxes.append((box, "water")) #(hitbox, type of item)
for pos in tree_pos:
    box = pygame.Rect(pos[0], pos[1], 16, 16)
    hitboxes.append((box, "tree")) #(hitbox, type of item)

x = 0
y = 0
adam = Person(person_img, x, y)
can_build = True
delta_time = .1
font = pygame.font.Font(None, size = 30)
#structure from pygame documentation
while running:
    screen.fill((255,255,255))
    
    adam.water -= 5 * delta_time
    adam.food -= 5 * delta_time
    adam.shelter -= 5 * delta_time
    if adam.food < 0 or adam.water < 0 or adam.shelter < 0:
        running = False

    prompt = f"Food: {adam.food:.1f}. Water: {adam.water:.1f}\n Wood: {adam.wood}, Shelter: {adam.shelter}"
    text = font.render(prompt, True, (0,0,0))
    screen.blit(text, (0,0))

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
    if keys[pygame.K_SPACE]:
        if can_build and adam.wood == 1:
            adam.wood = 0
            house_pos.append((adam.x,adam.y))
            box = pygame.Rect(adam.x, adam.y, 16, 16)
            hitboxes.append((box, "house")) #(hitbox, type of item)

            
    hitbox = pygame.Rect(adam.x, adam.y, 16, 16)
    for i in hitboxes:
        if hitbox.colliderect(i[0]):
            if i[1] == "food":
                adam.food = 60
                #food can only be used once
                position = (i[0].left, i[0].top)
                fruit_pos.remove(position)
                hitboxes.remove(i)
            if i[1] == "water":
                adam.water = 20
            if i[1] == "tree":
                adam.wood = 1
            if i[1] == "house":
                adam.shelter = 10
            can_build = False
        else:
            can_build = True


        
    # RENDER YOUR GAME HERE
    #places fruit, water, and trees
    for pos in fruit_pos:
        screen.blit(fruit_img, pos)
    for pos in water_pos:
        screen.blit(water_img, pos)
    for pos in tree_pos:
        screen.blit(tree_img, pos)
    for pos in house_pos:
        screen.blit(house_img, pos)

    screen.blit(adam.image, (adam.x,adam.y))
        
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)
    delta_time = clock.tick(60) / 1000
    delta_time= max(.001, min(.1, delta_time))

pygame.quit()