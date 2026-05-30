import pygame
import sys
import os
clock = pygame.time.Clock()
pygame.init()

def resource_path(path):
 if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, path)
 return os.path.join(os.path.abspath("."), path)

player_height = 583
player_width = 409
player_stop = pygame.transform.scale(pygame.image.load(resource_path("assets/img/player_down/player_stop.png")),(player_width,player_height))

screen_width = 1024 # переменная ширины экрана
screen_height = 768 #  переменая высоты экрана

vrag_privedenie_width = 120
vrag_privedenie_height = 125
list_privedenie = [

]

# эта команда которая создаёт окно с задаными порамитрами ширины и высоты
screen = pygame.display.set_mode((screen_width, screen_height))
# эта команда создаёт название окна
pygame.display.set_caption("JUST A HARDCORE GAME")

bullet = pygame.transform.scale(pygame.image.load(resource_path("assets/img/bullet_1.jpg")),(60,33)).convert_alpha()
bullet_list = [

]

screen_fon = pygame.image.load(resource_path("assets/img/fon.jpg"))
vrag_privedenie = pygame.transform.scale(pygame.image.load(resource_path("assets/img/ghost.png")),(vrag_privedenie_width,vrag_privedenie_height))

icon = pygame.image.load(resource_path("assets/img/vecteezy_imaginative-and-lovable-game-character-for-tshirt-graphic_27294895.png"))
player_walk_left = [
    pygame.transform.scale(pygame.image.load(resource_path("assets/img/player_left/9.png")),(player_width,player_height)),
    pygame.transform.scale(pygame.image.load(resource_path("assets/img/player_left/10.png")),(player_width,player_height)),
    pygame.transform.scale(pygame.image.load(resource_path("assets/img/player_left/11.png")),(player_width,player_height)),
    pygame.transform.scale(pygame.image.load(resource_path("assets/img/player_left/12.png")),(player_width,player_height))

]
player_walk_right = [

    pygame.transform.scale(pygame.image.load(resource_path("assets/img/player_right/5 (2).png")),(player_width,player_height)),
    pygame.transform.scale(pygame.image.load(resource_path("assets/img/player_right/6.png")),(player_width,player_height)),
    pygame.transform.scale(pygame.image.load(resource_path("assets/img/player_right/7.png")),(player_width,player_height)),
    pygame.transform.scale(pygame.image.load(resource_path("assets/img/player_right/8.png")),(player_width,player_height))

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

prived_timer = pygame.USEREVENT + 1
pygame.time.set_timer(prived_timer,3000)

game_play = True

loss_text = pygame.font.Font(
    resource_path("assets/texts/ofont.ru_Roboto.ttf"),
    40
)
restart_text = loss_text.render("ИГРАЙ ЗАНАВА,",False,(255,255,255))
text = loss_text.render("ТЫ ШИШ",False,(255,255,255))
button_restart = restart_text.get_rect(topleft = (370,300))

# Main game loop
# это главный игровой цикл который продолжает работать и следит за обновлениями в игре и событиями типа выхода из игры
while True:
    screen.blit(screen_fon,(fon_x,0))
    screen.blit(screen_fon,(fon_x + 1200,0))

    if game_play:
        
        # исправление 1
        player_hitbox = pygame.Rect(player_x + 160, player_y + 230, 80, 120)

        if list_privedenie:
            for (index, element) in enumerate(list_privedenie):
                screen.blit(vrag_privedenie,element)
                element.x = element.x - 10

                # исправление 2
                ghost_hitbox = pygame.Rect(element.x + 20, element.y + 20, 80, 70)

                if element.x < -250:
                    list_privedenie.pop(index)
                if player_hitbox.colliderect(element):
                    game_play = False
                    print("ты шиш?")

                # показать хитбокс врагов
                pygame.draw.rect(screen, (0, 255, 0), ghost_hitbox, 2)

        # показать хитбокс игрока
        pygame.draw.rect(screen, (255, 0, 0), player_hitbox, 2)

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

        if keys[pygame.K_RSHIFT]:
            bullet_list.append(bullet.get_rect(topleft = (player_x + 250,player_y + 260)))
            
        if bullet_list:
            for (index,atbullet) in enumerate(bullet_list):
                screen.blit(bullet,(atbullet.x,atbullet.y))
                atbullet.x = atbullet.x + 60
                if atbullet.x >= screen_width:
                        bullet_list.pop(index)
                if list_privedenie:
                    for (prindex,vrag) in enumerate(list_privedenie):
                        if atbullet.colliderect(vrag):
                            bullet_list.pop(index)
                            list_privedenie.pop(prindex)

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
    else:
        screen.fill((0,0,0))
        screen.blit(text,(440,400))
        screen.blit(restart_text,button_restart)
        mouse = pygame.mouse.get_pos()
        if button_restart.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            game_play = True
            player_x = 280
            list_privedenie.clear()
            bullet_list.clear()

    pygame.display.update()
    # этот цикл следит за выход из игры
    for event in pygame.event.get():
        if event.type == prived_timer:
            list_privedenie.append(vrag_privedenie.get_rect(topleft = (1060,460)))
            print(list_privedenie)
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    clock.tick(13)