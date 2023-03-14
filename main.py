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
# PlayerState[1] = ↑, PlayerState[2] = ↓, PlayerState[3] = <-, PlayerState[4] = ->
PlrY = 8
PlrX = 350
PlayerState_1 = pygame.image.load(f"PlayerState[1].png")
PlayerState_2 = pygame.image.load(f"PlayerState[2].png")
PlayerState_3 = pygame.image.load(f"PlayerState[3].png")
PlayerState_4 = pygame.image.load(f"PlayerState[4].png")
PlayerState = 1
CurrentPlayerState = PlayerState_1


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

        if event.type == pygame.KEYDOWN:
            if event == pygame.K_w:
                PlayerState = 1
            if event == pygame.K_s:
                PlayerState = 2
            if event == pygame.K_a:
                PlayerState = 3
            if event == pygame.K_d:
                PlayerState = 4

        if event.type == pygame.KEYUP:
            pass
    
    if PlayerState == 1:
        CurrentPlayerState = PlayerState_1
    if PlayerState == 2:
        CurrentPlayerState = PlayerState_2
    if PlayerState == 3:
        CurrentPlayerState = PlayerState_3
    if PlayerState == 4:
        CurrentPlayerState = PlayerState_4
    screen.blit(CurrentPlayerState, (PlrX,PlrY))        
    
    pygame.display.flip()
    pygame.display.update()
pygame.quit()