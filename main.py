import pygame
import sys
clock = pygame.time.Clock()
pygame.init()

player_height = 583
player_width = 409
player_stop = pygame.transform.scale(pygame.image.load("img/player_down/player_stop.png"),(player_width,player_height))

screen_width = 1024 # переменная ширины экрана
screen_height = 768 #  переменая высоты экрана

vrag_privedenie_width = 120
vrag_privedenie_height = 125

# эта команда которая создаёт окно с задаными порамитрами ширины и высоты
screen = pygame.display.set_mode((screen_width, screen_height))
# эта команда создаёт название окна
pygame.display.set_caption("JUST A HARDCORE GAME")
screen_fon = pygame.image.load("img/fon.jpg")
vrag_privedenie = pygame.transform.scale(pygame.image.load("img/ghost.png"),(vrag_privedenie_width,vrag_privedenie_height))

icon = pygame.image.load("img/vecteezy_imaginative-and-lovable-game-character-for-tshirt-graphic_27294895.png")
player_walk_left = [
    pygame.transform.scale(pygame.image.load("img/player_left/9.png"),(player_width,player_height)),
    pygame.transform.scale(pygame.image.load("img/player_left/10.png"),(player_width,player_height)),
    pygame.transform.scale(pygame.image.load("img/player_left/11.png"),(player_width,player_height)),
    pygame.transform.scale(pygame.image.load("img/player_left/12.png"),(player_width,player_height))

]
player_walk_right = [

    pygame.transform.scale(pygame.image.load("img/player_right/5 (2).png"),(player_width,player_height)),
    pygame.transform.scale(pygame.image.load("img/player_right/6.png"),(player_width,player_height)),
    pygame.transform.scale(pygame.image.load("img/player_right/7.png"),(player_width,player_height)),
    pygame.transform.scale(pygame.image.load("img/player_right/8.png"),(player_width,player_height))

]

animation_start = 0

fon_x = 0

vrag_privedenie_x = 1040
vrag_privedenie_y = 450

player_speed = 20
player_x = 280
player_y = 260
is_jump = False
jump_height = 10

#fon_sound = pygame.mixer.Sound('sounds/')
#fon_sound.play()

pygame.display.set_icon(icon)

# Main game loop
# это главный игровой цикл который продолжает работать и следит за обновлениями в игре и событиями типа выхода из игры
while True:
    screen.blit(screen_fon,(fon_x,0))
    screen.blit(screen_fon,(fon_x + 1200,0))

    screen.blit(vrag_privedenie,(vrag_privedenie_x,vrag_privedenie_y))
    player_hitbox = player_stop.get_rect(topleft = (player_x,player_y))
    vrag_privedenie_hitbox = vrag_privedenie.get_rect(topleft = (vrag_privedenie_x,vrag_privedenie_y))
    if player_hitbox.colliderect(vrag_privedenie_hitbox):
        print("шиш?")

    keys = pygame.key.get_pressed()
    #условие прорисовки
    if keys[pygame.K_LEFT]:
        screen.blit(player_walk_left[animation_start],(player_x,player_y))
    elif keys[pygame.K_RIGHT]:
        screen.blit(player_walk_right[animation_start],(player_x,player_y))
    else:
        screen.blit(player_stop,(player_x,player_y))

    #условие передвижения    
    if keys[pygame.K_LEFT] and player_x > -150:
        player_x = player_x - player_speed
        print(player_x)

    elif keys[pygame.K_RIGHT] and player_x < 770:
        player_x = player_x + player_speed
        print(player_x)

    if not is_jump:
        if keys[pygame.K_SPACE]:
            is_jump = True
            print('прыжок')
    else:
        if jump_height >= -10:
            if jump_height > 0:
                player_y = player_y - (jump_height**2) / 2
            else:
              player_y = player_y + (jump_height**2) / 2  
            jump_height = jump_height - 1
        else:
            is_jump = False
            jump_height = 10
    if animation_start == 3:
        animation_start = 0
    else:
        animation_start = animation_start + 1
    fon_x = fon_x - 5
    if fon_x == -1200:
        fon_x = 0
    vrag_privedenie_x = vrag_privedenie_x - 10
    pygame.display.update()
    # этот цикл следит за выход из игры
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    clock.tick(13)

