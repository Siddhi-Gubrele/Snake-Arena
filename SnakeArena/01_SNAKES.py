import os
import pygame
from random import randint
pygame.mixer.init()
x =  pygame.init()
pygame.font.get_fonts()

#Creating Game Screen
screen = pygame.display.set_mode((800,750))
pygame.display.set_caption("SNAKE ARENA")
pygame.display.update()

#DECORATIONS
bgimg = pygame.image.load("C:\\Users\Sparsh Ranjan\Desktop\\New folder\\01a_back.jpg")
bgimg = pygame.transform.scale(bgimg,(800,750)).convert_alpha()
wel = pygame.image.load("C:\\Users\Sparsh Ranjan\Desktop\\New folder\\01a_wall.webp")
wel = pygame.transform.scale(wel,(800,750)).convert_alpha()
end = pygame.image.load("C:\\Users\Sparsh Ranjan\Desktop\\New folder\\01a_game01.webp")
end = pygame.transform.scale(end,(800,750)).convert_alpha()


# Colours in game screen
white = (255,255,255)
red = (255,0,0)
blue = (0,255,0)
black = (0,0,0)
uk = (0,120,0)
yellow = (0,255,255)

write = pygame.font.SysFont('comicsansms',35)
clock = pygame.time.Clock()

def screen_text(text,color,x,y):
    on_screen = write.render(text,True,color)
    screen.blit(on_screen,[x,y])

def plot_snake(screen,color,snk_list,snake_size):
    for x,y in snk_list:
        pygame.draw.rect(screen, color, [x, y, snake_size, snake_size])

def welcome():
    game_end = False
    while not game_end:
        
        screen.fill((190,40,0))
        screen.blit(wel,(0,0))
        screen_text('WELCOME TO SNAKES',black,130,100)
        screen_text('PRESS SPACEBAR TO START',black,90,140)
        
               
        for steps in pygame.event.get():
            
            #pygame.mixer.music.load('')
            #pygame.mixer.music.play()
            if steps.type== pygame.QUIT:
                game_end = True

            if steps.type == pygame.KEYDOWN:
                if steps.key == pygame.K_SPACE:
                    pygame.mixer.music.load("C:\\Users\Sparsh Ranjan\Desktop\\New folder\\01a_ingame.mp3")
                    pygame.mixer.music.play()
                    ori_game()
                

        pygame.display.update() 
        clock.tick(69)

def ori_game():
    #Creating game variable
    game_over, game_end = False, False
    velo_x, velo_y  = 0, 0
    snake_x,snake_y = 25, 35
    food_x, food_y = randint(5,600), randint(50,600)
    score = 0
    speed = 2
    level_up = 0
    snake_size = 20
    fps = 100
    snk_list=[]
    snk_len=1
    high ='k'

    if(not os.path.exists("C:\\Users\Sparsh Ranjan\Desktop\\New folder\\01a_maximum.txt")):
        with open("C:\\Users\Sparsh Ranjan\Desktop\\New folder\\01a_maximum.txt",'w') as f:
            f.write('0')

    with open("C:\\Users\Sparsh Ranjan\Desktop\\New folder\\01a_maximum.txt",'r') as f:
        high = f.read()
    
    while not game_end:
        
        if game_over:
                screen.fill(black)
                screen.blit(end,(0,0))
                screen_text("YOUR SCORE IS  "+ str(score),white,375,610)
                screen_text("PRESS ENTER TO CONTINUE",white,270,660)

                for steps in pygame.event.get():

                    if steps.type == pygame.QUIT:
                        game_end = True

                    if steps.type == pygame.KEYDOWN:
                        if steps.key == pygame.K_RETURN:
                            pygame.mixer.music.load("C:\\Users\Sparsh Ranjan\Desktop\\New folder\\01a_ingame.mp3")
                            pygame.mixer.music.play()
                            ori_game() 
        else :
            
            for steps in pygame.event.get():
                if steps.type == pygame.QUIT:
                    game_end = True 

                 # It determines whether a key is pressed or not:
                if steps.type == pygame.KEYDOWN: 

                    if steps.key == pygame.K_RIGHT:
                        velo_x = speed
                        velo_y=0

                    if steps.key == pygame.K_LEFT:
                        velo_x = -speed
                        velo_y=0

                    if steps.key == pygame.K_UP:
                        velo_y = -speed
                        velo_x=0

                    if steps.key == pygame.K_DOWN:
                        velo_y = speed
                        velo_x=0
                    if steps.key == pygame.K_a:
                        score +=80

            snake_x = velo_x + snake_x
            snake_y = velo_y + snake_y
                        
            if abs(snake_x - food_x)<12 and abs(snake_y - food_y)<12:
                score += 10
                snk_len += 5
                level_up = score
                food_x = randint(5,600)
                food_y = randint(50,600)

                if level_up%100 == 0:
                    speed += 1

                if score > int(high):
                    high = score
                    with open("C:\\Users\Sparsh Ranjan\Desktop\\New folder\\01a_maximum.txt",'w') as f:
                        f.write(str(high))
            
            screen.fill(white)
            screen.blit(bgimg,(0,0))

            screen_text("SCORE : "+ str(score) + "      High Score : " + str(high),yellow,5,5)

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_len:
                del snk_list[0]

            if snake_x<0 or snake_y <0 or snake_x >770 or snake_y> 770 :
                pygame.mixer.music.load("C:\\Users\Sparsh Ranjan\Desktop\\New folder\\01a_end.mp3")
                pygame.mixer.music.play()
                game_over = True
            if head in snk_list[:-1]:
                pygame.mixer.music.load("C:\\Users\Sparsh Ranjan\Desktop\\New folder\\01a_end.mp3")
                pygame.mixer.music.play()
                game_over = True
                    
            plot_snake(screen,red,snk_list,snake_size)
            pygame.draw.rect(screen, white, [food_x, food_y,12,12])

        pygame.display.update()        
        clock.tick(fps)
    
    pygame.quit()

welcome()    