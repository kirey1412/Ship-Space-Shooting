import pygame, os
pygame.font.init()
pygame.mixer.init()
pygame.init()
WIDTH, HEIGHT = 700, 650
SW, SH = 50, 50
screen=pygame.display.set_mode((WIDTH,HEIGHT))
title=pygame.display.set_caption("Shooting Ships")

space=pygame.image.load("spacebg.png")
yellowship=pygame.image.load("yellowship.png")
redship=pygame.image.load("redship.png")

space=pygame.transform.scale(space, (WIDTH, HEIGHT))
yellowship=pygame.transform.scale(yellowship, (SW, SH))
yellowship=pygame.transform.rotate(yellowship, (90))
redship=pygame.transform.rotate(pygame.transform.scale(redship, (SW, SH)),-90)

border=pygame.Rect(WIDTH/2-5,0,10,HEIGHT)
def draw():
    screen.blit(space, (0,0))
    pygame.draw.rect(screen, "black", border)
    screen.blit(yellowship, (50, HEIGHT/2))
    screen.blit(redship, (WIDTH-50, HEIGHT/2))
    pygame.display.update()

draw()