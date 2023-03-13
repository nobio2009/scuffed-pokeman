import pygame
from colors import *
from movement import Movement

pygame.init()

WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Scuffed pokemon in python')
fps = 60
timer = pygame.time.Clock()
font = pygame.font.Font('freesansbold.ttf', 18)

#player
# PlayerState[1] = ↓, PlayerState[2] = ↑, PlayerState[3] = <-, PlayerState[4] = ->
player_sprite = pygame.image.load()

class Button:
    def __init__(self, text, x_pos, y_pos, enabled):
        self.text = text
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.enabled = enabled
        self.draw()

    def draw(self):
        button_text = font.render(self.text, True, 'black')
        button_rect = pygame.rect.Rect((self.x_pos, self.y_pos), (150, 25))
        if self.enabled:
            if self.check_clicked():
                pygame.draw.rect(screen, 'dark gray', button_rect, 0, 5)
            else:
                pygame.draw.rect(screen, 'light gray', button_rect, 0, 5)
        else:
            pygame.draw.rect(screen, 'black', button_rect, 0, 5)
        pygame.draw.rect(screen, 'black', button_rect, 2, 5)
        screen.blit(button_text, (self.x_pos + 3, self.y_pos + 3))

    def check_clicked(self):
        mouse_pos = pygame.mouse.get_pos()
        left_click = pygame.mouse.get_pressed()[0]
        button_rect = pygame.rect.Rect((self.x_pos, self.y_pos), (150, 25))

        if left_click and button_rect.collidepoint(mouse_pos) and self.enabled:
            return True
        else:
            return False

run = True
while run:
    #vital functions
    screen.fill('white')
    timer.tick(fps)


    #Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break
    
    pygame.display.flip()
    pygame.display.update()
pygame.quit()