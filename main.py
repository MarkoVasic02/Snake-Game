import pygame, time, random, sys
from os import system
 
pygame.init()
system('cls')
 
# colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
blue = (54, 64, 170)

# display size
dis_width = 800
dis_height = 600
 
# setting up display and window name
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game BRO')

# list containing random coordinates of the fruit to be generated at
fruit_loc = [random.randrange(1, (dis_width//40)) * 40, random.randrange(1, (dis_height//30)) * 30]

# condition to run the game loop
finish_game = False
over = False

# snake coordinates at the start
x1 = dis_width/2
y1 = dis_height/2
snake_position = [x1, y1]
snake_body = [
              snake_position, 
             [snake_position[0] - 10,snake_position[1]], 
             [snake_position[0] - 20, snake_position]
             ]
 
# snake speed
x1_change = 0       
y1_change = 0

# score
score = 0

# snake length
snake_length = 1
# list of coordinates of the snake bodies parts
snake_list = []

clock = pygame.time.Clock()


# function takes every element of the
# snake_list and draws a rect for each
def our_snake(snake_list):
    if snake_length != 1:
        for x in snake_list:
            pygame.draw.rect(dis, black, [x[0], x[1], 20, 20])
    else:
        pass
    

main_font = pygame.font.SysFont('times new roman', 90)
small_main_font = pygame.font.SysFont('times new roman', 20)


def game_over():
    global over, finish_game
    while over:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.QUIT:
                    finish_game = True
                    over = False
                elif event.key == ord('n'):
                    over = False
                elif event.key == ord('q'):
                    finish_game = True
                    over = False
        dis.fill(black)
        game_over_surface = main_font.render('YOU DIED', True, red)
        game_over_rect = game_over_surface.get_rect()
        game_over_rect.midtop = (dis_width/2, dis_height/4)
        dis.blit(game_over_surface, game_over_rect)
        show_score(1, red, size = 20)
        pygame.display.update()


# Score
def show_score(choice, color = white, font="times new roman", name = "VibesV.ttf", size = 20):
    if choice == 1:
        # system
        sys_score_font = pygame.font.SysFont(font, size)
        sys_score_surface = sys_score_font.render('Score : ' + str(score), True, color)
        sys_score_rect = sys_score_surface.get_rect()
        sys_score_rect.midtop = (dis_width/2, dis_height/1.25)
        dis.blit(sys_score_surface, sys_score_rect)
    else:
        # custom
        cus_score_font = pygame.font.Font(name, size)
        cus_score_surface = cus_score_font.render('Score : ' + str(score), True, color)
        cus_score_rect = cus_score_surface.get_rect()
        cus_score_rect.midtop = (dis_width/10, 15)        
        dis.blit(cus_score_surface, cus_score_rect)

# game loop
while not finish_game:
    game_over()
    # listening for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish_game = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -10
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = 10
                y1_change = 0
            elif event.key == pygame.K_UP:
                y1_change = -10
                x1_change = 0
            elif event.key == pygame.K_DOWN:
                y1_change = 10
                x1_change = 0

    # if snake touches boundaries game ends
    if snake_position[0] >= dis_width or snake_position[0] <= 0 or snake_position[1] >= dis_height or snake_position[1] <= 0:
        over = True

    # changing snake coordinates with every frame
    snake_position[0] += x1_change
    snake_position[1] += y1_change

    # colloring display
    dis.fill(blue)
    #show score
    show_score(choice=0)

    # drawing player and food at its above defined location
    player = pygame.draw.rect(dis, black, [snake_position[0], snake_position[1], 20, 20])
    food = pygame.draw.rect(dis, red, [fruit_loc[0], fruit_loc[1], 20, 20])

    # appending lists of coordinates to snake_list list
    # and then emptying the snake_head list in the next frame
    snake_head = []
    snake_head.append(snake_position[0])
    snake_head.append(snake_position[1])
    snake_list.append(snake_head)

    # snake_list can have only one element
    if len(snake_list) > snake_length:
        del snake_list[0]

    # if any of the body parts had the same
    # coordinates as the head game ends
    for x in snake_list[:-1]:
        if x == snake_head:
            over = True
            snake_length = 1
            score = 0

    our_snake(snake_list)

    pygame.display.update()

    # if snake gets the food, new random
    # location for the food is generated
    if player.colliderect(food):
        fruit_loc = [random.randrange(1, (dis_width//40)) * 40, random.randrange(1, (dis_height//30)) * 30]
        snake_length += 1
        score += 1
    
    pygame.display.update()
 
    clock.tick(30)

pygame.quit()
quit()