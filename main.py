import pygame
import sys

pygame.init()

screen_width = 1024 # переменная ширины экрана
screen_height = 768 #  переменая высоты экрана
# эта команда которая создаёт окно с задаными порамитрами ширины и высоты
screen = pygame.display.set_mode((screen_width, screen_height))
# эта команда создаёт название окна
pygame.display.set_caption("JUST A HARDCORE GAME")
icon = pygame.image.load("img/7748153.png")
player = pygame.image.load("img/sprite-sheet.png")
pygame.display.set_icon(icon)

# Main game loop
# это главный игровой цикл который продолжает работать и следит за обновлениями в игре и событиями типа выхода из игры
while True:
    screen.fill((10,0,12))
    screen.blit(player,(300,250))
    pygame.display.update()
    # этот цикл следит за выход из игры
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

