import pygame
import sys
clock = pygame.time.Clock()
pygame.init()
player_height = 583
player_width = 409
screen_width = 1024 # переменная ширины экрана
screen_height = 768 #  переменая высоты экрана
# эта команда которая создаёт окно с задаными порамитрами ширины и высоты
screen = pygame.display.set_mode((screen_width, screen_height))
# эта команда создаёт название окна
pygame.display.set_caption("JUST A HARDCORE GAME")
screen_fon = pygame.image.load("img/fon.jpg")
icon = pygame.image.load("img/vecteezy_imaginative-and-lovable-game-character-for-tshirt-graphic_27294895.png")
player_walk_left = [
    pygame.transform.scale(pygame.image.load("img/player_left/9.png"),(player_width,player_height)),
    pygame.transform.scale(pygame.image.load("img/player_left/10.png"),(player_width,player_height)),
    pygame.transform.scale(pygame.image.load("img/player_left/11.png"),(player_width,player_height)),
    pygame.transform.scale(pygame.image.load("img/player_left/12.png"),(player_width,player_height))

]
player_walk_right = [
    pygame.image.load("img/player_right/5 (2).png"),
    pygame.image.load("img/player_right/6.png"),
    pygame.image.load("img/player_right/7.png"),
    pygame.image.load("img/player_right/8.png")
]

animation_start = 0

fon_x = 0

pygame.display.set_icon(icon)

# Main game loop
# это главный игровой цикл который продолжает работать и следит за обновлениями в игре и событиями типа выхода из игры
while True:
    screen.blit(screen_fon,(fon_x,0))
    screen.blit(screen_fon,(fon_x - 1200,0))
    screen.blit(player_walk_left[animation_start],(280,200))
    if animation_start == 3:
        animation_start = 0
    else:
        animation_start = animation_start + 1
    fon_x = fon_x + 5
    if fon_x == 1200:
        fon_x = 0
    pygame.display.update()
    # этот цикл следит за выход из игры
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    clock.tick(13)
