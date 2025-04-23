import pygame, time
from pygame.locals import *
pygame.init()
screen=pygame.display.set_mode((700,600))
title=pygame.display.set_caption("Feeding Fish")

fish_x, fish_y=300,0
bg=pygame.image.load("aquarium.jpg")
fish=pygame.image.load("fish.png")

while fish_y < 600:
    screen.blit(bg, (0,0))
    screen.blit(fish, (fish_x, fish_y))
    pygame.display.flip()
    for i in pygame.event.get():
        print(i)
        if i.type==pygame.QUIT:
         pygame.quit()
        if i.type==pygame.KEYDOWN:
            print(i.key)
            if i.key==K_UP and fish_y > 0:
                fish_y-=5
            elif i.key==K_DOWN:
                fish_y+=5
            elif i.key==K_LEFT and fish_x > 0:
                fish_x-=5
            elif i.key==K_RIGHT and fish_x < 700:

                fish_x+=5
            else:
                break
    fish_y+=1
    time.sleep(0.05)

