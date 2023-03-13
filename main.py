import pygame
from movement import Movement

pygame.init()
Hight = 600
Width = 800
#[Width, Hight]
screen = pygame.display.set_mode((800, 600))

player_image = pygame.image.load("player.png")
x = 8
y = 278

running = True
while running:
    screen.fill("White")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break

    player_sprite = screen.blit(player_image, (x,y))
pygame.quit()