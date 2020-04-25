# 피하기 게임 - 플레이어 이미지를 화면 중앙 하단에 출력

import pygame

WHITE = (255,255,255)
BLACK = (0,0,0)

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)

player_url = 'resources/d_images/people.png'
player_img = pygame.image.load(player_url)
player_pos = player_img.get_rect()

player_pos.left = SCREEN_WIDTH // 2 -(player_img.get_width() // 2)
player_pos.top = SCREEN_HEIGHT - player_img.get_height()

while True:
    screen.fill(WHITE)

    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        exit()

    screen.blit(player_img, player_pos)
    pygame.display.flip()







