import pygame
import random

pygame.init()

width = 500
height = 500

game_window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Shooter")

# Game variables
exit_game = False
game_over = False
character_x = 50
character_y = 50
width_character = 15
height_character = 15

velocity_x = 20
velocity_y = 20
shooting_velocity = 1

enemy_x = random.randint(10, 490)
enemy_y = random.randint(10, 490)
random_shoot = 1

hit_check_enemy = False
hit_check_player = False
clock = pygame.time.Clock()
fps = 1000


def print(game_window, colour, x, y, width_character, height_character):
    pygame.draw.rect(game_window, colour, [x, y, width_character, height_character])


def shoot_right_character(x, y, enemy_x, enemy_y):
    global hit_check_enemy
    while(True):
        print(game_window, (0, 0, 0), x, y, width_character/2, height_character/2)
        pygame.display.update()
        x += shooting_velocity
        if(x >= width):
            break
        if(abs(enemy_x - x) <= 10 and abs(enemy_y - y) <= 10):
            hit_check_enemy = True
            break

def shoot_left_character(x, y, enemy_x, enemy_y):
    global hit_check_enemy
    while(True):
        print(game_window, (0, 0, 0), x, y, width_character/2, height_character/2)
        pygame.display.update()
        x -= shooting_velocity
        if(x <= 0):
            break
        if(abs(enemy_x - x) <= 10 and abs(enemy_y - y) <= 10):
            hit_check_enemy = True
            break


def shoot_up_character(x, y, enemy_x, enemy_y):
    global hit_check_enemy
    while(True):
        print(game_window, (0, 0, 0), x, y, width_character/2, height_character/2)
        pygame.display.update()
        y -= shooting_velocity
        if(y <= 0):
            break
        if(abs(enemy_x - x) <= 10 and abs(enemy_y - y) <= 10):
            hit_check_enemy = True
            break

def shoot_down_character(x, y, enemy_x, enemy_y):
    global hit_check_enemy
    while(True):
        print(game_window, (0, 0, 0), x, y, width_character/2, height_character/2)
        pygame.display.update()
        y += shooting_velocity
        if(y >= height):
            break
        if(abs(enemy_x - x) <= 10 and abs(enemy_y - y) <= 10):
            hit_check_enemy = True
            break

# Enemy
def shoot_top_left_enemy(x, y, character_x, character_y):
    global hit_check_player
    while(True):
        print(game_window, (255, 0, 0), x, y, width_character/2, height_character/2)
        pygame.display.update()
        x -= shooting_velocity
        y -= shooting_velocity
        if(x <= 0 or y <= 0):
            break
        if(abs(character_x - x) <= 10 and abs(character_y - y) <= 10):
            hit_check_player = True
            break
def shoot_top_right_enemy(x, y, character_x, character_y):
    global hit_check_player
    while(True):
        print(game_window, (255, 0, 0), x, y, width_character/2, height_character/2)
        pygame.display.update()
        x += shooting_velocity
        y -= shooting_velocity
        if(x >= width or y <= 0):
            break
        if(abs(character_x - x) <= 10 and abs(character_y - y) <= 10):
            hit_check_player = True
            break

def shoot_bottom_left_enemy(x, y, character_x, character_y):
    global hit_check_player
    while(True):
        print(game_window, (255, 0, 0), x, y, width_character/2, height_character/2)
        pygame.display.update()
        x -= shooting_velocity
        y += shooting_velocity
        if(x <= 0 or y >= height):
            break
        if(abs(character_x - x) <= 10 and abs(character_y - y) <= 10):
            hit_check_player = True
            break

def shoot_bottom_right_enemy(x, y, character_x, character_y):
    global hit_check_player
    while(True):
        print(game_window, (255, 0, 0), x, y, width_character/2, height_character/2)
        pygame.display.update()
        x += shooting_velocity
        y += shooting_velocity
        if(x >= width or y >= height):
            break
        if(abs(character_x - x) <= 10 and abs(character_y - y) <= 10):
            hit_check_player = True
            break

def shoot_right_enemy(x, y, character_x, character_y):
    global hit_check_player
    while(True):
        print(game_window, (255, 0, 0), x, y, width_character/2, height_character/2)
        pygame.display.update()
        x += shooting_velocity
        if(x >= width):
            break
        if(abs(character_x - x) <= 10 and abs(character_y - y) <= 10):
            hit_check_player = True
            break

def shoot_left_enemy(x, y, character_x, character_y):
    global hit_check_player
    while(True):
        print(game_window, (255, 0, 0), x, y, width_character/2, height_character/2)
        pygame.display.update()
        x -= shooting_velocity
        if(x <= 0):
            break
        if(abs(character_x - x) <= 10 and abs(character_y - y) <= 10):
            hit_check_player = True
            break


def shoot_up_enemy(x, y, character_x, character_y):
    global hit_check_player
    while(True):
        print(game_window, (255, 0, 0), x, y, width_character/2, height_character/2)
        pygame.display.update()
        y -= shooting_velocity
        if(y <= 0):
            break
        if(abs(character_x - x) <= 10 and abs(character_y - y) <= 10):
            hit_check_player = True
            break

def shoot_down_enemy(x, y, character_x, character_y):
    global hit_check_player
    while(True):
        print(game_window, (255, 0, 0), x, y, width_character/2, height_character/2)
        pygame.display.update()
        y += shooting_velocity
        if(y >= height):
            break
        if(abs(character_x - x) <= 10 and abs(character_y - y) <= 10):
            hit_check_player = True
            break


while not exit_game:
    pygame.mixer.Channel(0).play(pygame.mixer.Sound("laser.mp3"))
    
    game_window.fill((0, 255, 255))
    print(game_window, (255, 0, 0), enemy_x, enemy_y, width_character, height_character)
    print(game_window, (0, 0, 0), character_x,character_y, width_character, height_character)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if(character_x >= 0):
                    character_x -= velocity_x
            elif event.key == pygame.K_RIGHT:
                if(character_x <= width - width_character):
                    character_x += velocity_x
            elif event.key == pygame.K_UP:
                if(character_y >= 0):
                    character_y -= velocity_y
            elif event.key == pygame.K_DOWN:
                if(character_y <= height - height_character):
                    character_y += velocity_y
            elif(event.key == pygame.K_d):
                shoot_right_character(character_x + 20, character_y + width_character/3.5, enemy_x, enemy_y)
                pygame.mixer.Channel(0).play(pygame.mixer.Sound("laser.mp3"))

            elif(event.key == pygame.K_a):
                shoot_left_character(character_x - 12, character_y + width_character/3.5, enemy_x, enemy_y)
                pygame.mixer.Channel(0).play(pygame.mixer.Sound("laser.mp3"))

            elif(event.key == pygame.K_w):
                shoot_up_character(character_x + height_character/3.5, character_y - 12, enemy_x, enemy_y)
                pygame.mixer.Channel(0).play(pygame.mixer.Sound("laser.mp3"))

            elif(event.key == pygame.K_x):
                shoot_down_character(character_x + height_character/3.5, character_y + 20, enemy_x, enemy_y)
                pygame.mixer.Channel(0).play(pygame.mixer.Sound("laser.mp3"))


        
    random_shoot =  random.randint(1,150)

    if(character_x < enemy_x and character_y < enemy_y):
        if(random_shoot == 1):
            shoot_up_enemy(enemy_x , enemy_y, character_x, character_y)
        elif(random_shoot == 2):
            shoot_left_enemy(enemy_x , enemy_y, character_x, character_y)
        elif(random_shoot == 3):
            shoot_top_left_enemy(enemy_x , enemy_y, character_x, character_y)

    elif(character_x < enemy_x and character_y > enemy_y):
        if(random_shoot == 1):
            shoot_down_enemy(enemy_x , enemy_y, character_x, character_y)
        elif(random_shoot == 2):
            shoot_left_enemy(enemy_x , enemy_y, character_x, character_y)
        elif(random_shoot == 3):
            shoot_bottom_left_enemy(enemy_x , enemy_y, character_x, character_y)

    elif(character_x > enemy_x and character_y < enemy_y):
        if(random_shoot == 1):
            shoot_up_enemy(enemy_x , enemy_y, character_x, character_y)
        elif(random_shoot == 2):
            shoot_right_enemy(enemy_x , enemy_y, character_x, character_y)
        elif(random_shoot == 3):
            shoot_top_right_enemy(enemy_x , enemy_y, character_x, character_y)
    else:
        if(random_shoot == 1):
            shoot_down_enemy(enemy_x , enemy_y, character_x, character_y)
        elif(random_shoot == 2):
            shoot_right_enemy(enemy_x , enemy_y, character_x, character_y)
        elif(random_shoot == 3):
            shoot_bottom_right_enemy(enemy_x , enemy_y, character_x, character_y)

    if(hit_check_enemy):
        enemy_x = random.randint(10, 490)
        enemy_y = random.randint(10, 490)
        hit_check_enemy = False

    elif(hit_check_player):
        character_x = random.randint(10, 490)
        character_y = random.randint(10, 490)
        hit_check_player = False

    clock.tick(fps)