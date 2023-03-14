import pygame
from colors import *
from save import *

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
PlayerLocation = CurrentLocation
CurrentPlayerState = PlayerState_1

#Collisions
def is_collided_with(self, sprite): return self.colliderect(sprite)

#Movement
speed = 2.5

def Movement(pygame, x,y):
    keys = pygame.key.get_pressed()
    file='player.png'
    if keys[pygame.K_w]:
        y-=speed
    elif keys[pygame.K_s]:
        y+=speed
    elif keys[pygame.K_d]:
        x+=speed
    elif keys[pygame.K_a]:
        x-=speed
    x,y = borders(x, y)
    return x,y,file

def borders(x, y):
    if x >= 650:
        x = 650
    elif x <= 51.5:
        x = 51.5
    if y <= 120:
        y=120
    elif y >= 440:
        y=440
    return x,y

#Initial background
locations = ['PlayerRoom', 'PlayerKitchen', 'Village', 'Bjarnes lab', 'Healing center']
if PlayerLocation == locations[0]:
    background = pygame.image.load('PlayerRoom.png')
elif PlayerLocation == locations[1]:
    background = pygame.image.load('PlayerKitchen.png')
else:
    pass

#saving
def save(location):
        f = open("save.py", "w")
        f.write(f"CurrentLocation = \"{location}\"" + "\n")
        f.close()

#Text Rendering
def DrawText(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

#Buttons
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
    screen.fill(TEAL)
    screen.blit(background, (0, 10))
    timer.tick(fps)

    #backgrounds
    locations = ['PlayerRoom', 'PlayerKitchen', 'Village', 'Bjarnes lab', 'Healing center']
    if PlayerLocation == locations[0]:
        background = pygame.image.load('PlayerRoom.png')
    elif PlayerLocation == locations[1]:
        background = pygame.image.load('PlayerKitchen.png')
    else:
        pass

    #Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                PlayerState = 1
            if event.key == pygame.K_s:
                PlayerState = 2
            if event.key == pygame.K_a:
                PlayerState = 3
            if event.key == pygame.K_d:
                PlayerState = 4

            if event.key == pygame.K_e:
                print(f'PlayerX: {PlrX} | PlayerY: {PlrY}')
                if PlrX >= 565.0 and PlrX <= 617.5 and PlrY == 120:
                    if PlayerLocation == 'PlayerRoom':
                        PlayerLocation = 'PlayerKitchen'

                    if PlayerLocation == 'PlayerKitchen':
                        PlayerLocation = 'PlayerRoom'

        if event.type == pygame.KEYUP:
            pass

    PlrX,PlrY,CurrentPlayerState = Movement(pygame, PlrX,PlrY)
    
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