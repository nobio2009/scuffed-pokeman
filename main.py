import pygame 

pygame.init()
Hight = 600
Width = 800
pygame.display.set_mode([Hight, Width])

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
pygame.quit()