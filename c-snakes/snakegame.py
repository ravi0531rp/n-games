import pygame
import random

# Initialize the game
pygame.init()

# Set the dimensions of the screen
size = (700, 500)
screen = pygame.display.set_mode(size)

# Set the title of the screen
pygame.display.set_caption("Snake Game")

# Set the color of the screen
black = (0, 0, 0)

# Set the font for displaying the score
font_style = pygame.font.SysFont(None, 50)

# Initialize the snake's starting position
snake_block = 10
snake_speed = 30

snake_list = [[100, 100]]
foodx = round(random.randrange(0, size[0]-10)/10.0)*10.0
foody = round(random.randrange(0, size[1]-10)/10.0)*10.0
food = [foodx, foody]

# Initialize the direction of the snake
direction = "right"
change_to = direction

clock = pygame.time.Clock()

score = 0

# Main loop of the game
while True:
    for event in pygame.event.get():
        # Check for the QUIT event
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        # Check for key presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = "up"
            if event.key == pygame.K_DOWN:
                change_to = "down"
            if event.key == pygame.K_LEFT:
                change_to = "left"
            if event.key == pygame.K_RIGHT:
                change_to = "right"

    # Make sure the snake cannot move in the opposite direction instantaneously
    if change_to == "up" and direction != "down":
        direction = "up"
    if change_to == "down" and direction != "up":
        direction = "down"
    if change_to == "left" and direction != "right":
        direction = "left"
    if change_to == "right" and direction != "left":
        direction = "right"

    # Move the snake by adding a block in the direction it is moving
    if direction == "up":
        snake_head = [snake_list[0][0], snake_list[0][1]]
        snake_list.insert(0, [snake_head[0], snake_head[1]-10])
    if direction == "down":
        snake_head = [snake_list[0][0], snake_list[0][1]]
        snake_list.insert(0, [snake_head[0], snake_head[1]+10])
    if direction == "left":
        snake_head = [snake_list[0][0], snake_list[0][1]]
        snake_list.insert(0, [snake_head[0]-10, snake_head[1]])
    if direction == "right":
        snake_head = [snake_list[0][0], snake_list[0][1]]
        snake_list.insert(0, [snake_head[0]+10, snake_head[1]])
        
    # If the snake hits the food, increase the score
    if snake_list[0][0] == food[0] and snake_list[0][1] == food[1]:
        food = []
        score += 1
        while food == []:
            foodx = round(random.randrange(0, size[0]-10)/10.0)*10.0
            foody = round(random.randrange(0, size[1]-10)/10.0)*10.0
            food = [foodx, foody]
            if food in snake_list:
                food = []
                
    else:
        snake_list.pop()

    # Check for collision with the boundaries
    if snake_list[0][0] >= size[0] or snake_list[0][0] < 0 or snake_list[0][1] >= size[1] or snake_list[0][1] < 0:
        pygame.quit()
        exit()
        
    # Check for collision with the snake's body
    for block in snake_list[1:]:
        if snake_list[0][0] == block[0] and snake_list[0][1] == block[1]:
            pygame.quit()
            exit()
            
    # Display the score
    score_text = font_style.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(score_text, [0,0])
    
    # Draw the snake and the food
    for x,y in snake_list:
        pygame.draw.rect(screen, (255,0,0), [x, y, snake_block, snake_block])
    pygame.draw.rect(screen, (0, 255, 0), [food[0], food[1], snake_block, snake_block])
    pygame.display.update()
    clock.tick(snake_speed)

pygame.quit()

