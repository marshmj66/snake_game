import random
import time
import os
import pygame
from pygame.locals import QUIT

pygame.init()
pygame.mixer.init()

start = False
death = 1
DISPLAYSURF = pygame.display.set_mode((800, 600))
sound = pygame.mixer.Sound(os.path.join('assests//Grenade+1.mp3'))
sound2 = pygame.mixer.Sound(os.path.join('assests','Gun+Silencer.mp3'))
background_sound = pygame.mixer.Sound(os.path.join('assests','Farming-By-Moonlight.mp3'))
DISPLAYSURF.fill("darkblue")
pygame.display.set_caption("Snake Game")
screen = pygame.Surface((200,300))
x = 0
y = 0
x_speed = 10
y_speed = 10

snake_size = 0
snake_body = []
part_popped = [-1,-1]

fX = round(random.randint(0, 800)/10.0)*10.0
fY = round(random.randint(0, 600)/10)*10.0

score = 0

clock = pygame.time.Clock()

class Start_Button:
    def __init__(self):
        pass

    def bliting(self,on):
        if on:
            self.start_btn = pygame.draw.rect(DISPLAYSURF, 'red', (700 / 2, 500 / 2, 75, 75), 0)
            self.smallfont = pygame.font.SysFont('Corbel', 35)
            self.text = self.smallfont.render('Start', True, 'black')
            DISPLAYSURF.blit(self.text, (700 / 2, 550 / 2))
    def cover_blit(self):
        self.start_btn = pygame.draw.rect(DISPLAYSURF, 'blue', (700 / 2, 500 / 2, 75, 75), 0)
        self.smallfont = pygame.font.SysFont('Corbel', 35)
        self.text = self.smallfont.render('Start', True, 'blue')
        DISPLAYSURF.blit(self.text, (700 / 2, 550 / 2))

class Snake:
    def __init__(self):
        pass
    def draw(self,n_x,n_y):
        for s in snake_body:
            snake = pygame.draw.rect(DISPLAYSURF, 'lightblue', ( s[0],s[1], 10, 10), 0)

    def move(self,x,y):
        print("moving")


class Food:
    def __init__(self):
        self.targetX = 0
        self.targetY = 0

    def draw(self,x,y):
        self.targetX = x
        self.targetY = y
        food = pygame.draw.rect(DISPLAYSURF, 'orange', (self.targetX, self.targetY, 10, 10), 0)

whole_game = True
game = True
background_sound.play()
while whole_game:
    player = Snake()
    food = Food()
    previous = []
    pygame.display.update()
    start_btn = Start_Button()
    if game:
        death = 1
        if start is False:
            print('button')
            start_btn.bliting(True)
        else:
            if -1 > x or x > 800 or -1 > y or y > 600:
                game = False
                print('game over')

            if len(snake_body) <= snake_size:
                snake_body.append((x,y))

            DISPLAYSURF.fill('blue')
            if x == fX and y == fY:
                fX = round(random.randint(0, 750) / 10.0) * 10.0
                fY = round(random.randint(0, 550) / 10.0) * 10.0
                sound.play()
                snake_size+=1
                score += 1
            player.draw(x,y)
            food.draw(fX,fY)
            x+= x_speed
            y+= y_speed

            font = pygame.font.Font(None, 35)
            text = font.render('Score ' + str(score), 1, 'white')
            DISPLAYSURF.blit(text, (0, 0))

            if part_popped[0] == x and part_popped[1] == y:
                print('game over')
                game = False

            print('postion',snake_body)
            if len(snake_body) > snake_size:
                del snake_body[0]
            if len(snake_body) > 0:
                part_popped = snake_body[-1]
                if part_popped in snake_body[:-1]:
                    game = False
    else:
        if death == 1:
            sound2.play()
            death = 0
        #sound2.stop()
        DISPLAYSURF.fill('blue')
        font = pygame.font.Font(None, 50)
        text = font.render('Game Over you have a Score of ' + str(score), 1, 'white')
        restart = font.render("Restart", 1, 'lightyellow')
        DISPLAYSURF.blit(text, (150, 200))
        DISPLAYSURF.blit(restart, (200, 300))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            if 353 <= mouse[0] <= 423 and 252 <= mouse[1] <= 320 and not start:
                start = True
                start_btn.cover_blit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                #DISPLAYSURF.fill('blue')
                y_speed = -10
                x_speed = 0

            if event.key == pygame.K_s:
                #DISPLAYSURF.fill('blue')
                y_speed = 10
                x_speed = 0
            if event.key == pygame.K_a:
                #DISPLAYSURF.fill('blue')

                x_speed = -10
                y_speed = 0
            if event.key == pygame.K_d:
                #DISPLAYSURF.fill('blue')
                x_speed = 10
                y_speed = 0
        if game == False:
            if event.type == pygame.MOUSEBUTTONDOWN:
                btn_restart = pygame.mouse.get_pos()
                if 203 <= btn_restart[0] <= 301 and 301 <= btn_restart[1] <= 328:
                    print(btn_restart)
                    x = 0
                    y = 0
                    x_speed = 10
                    y_speed = 10
                    snake_size = 0
                    snake_body = []
                    score = 0
                    background_sound.stop()
                    background_sound.play()
                    game = True



    clock.tick(15)