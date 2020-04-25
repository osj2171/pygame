# 피하기 게임
#  바이러스 이밎 그리기

import pygame
import random

WHITE = (255,255,255)
BLACK = (0,0,0)

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()

pygame.key.set_repeat(1)

player_url = 'resources/d_images/people.png'
player_img = pygame.image.load(player_url)
player_pos = player_img.get_rect(centerx = SCREEN_WIDTH//2,
                                 bottom = SCREEN_HEIGHT)

# 적 이미지 불러오기
enemy_url = 'resources/d_images/virus.png'
enemy_img = pygame.image.load(enemy_url)
#enemies = list()
enemies = []
for cnt in range(3):
    enemy_pos = enemy_img.get_rect(left=150*cnt +100, top=100)
    enemies.append(enemy_pos)
    print(enemy_pos)


while True:
    screen.fill(WHITE)

    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        exit()
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            player_pos.left -=5
        elif event.key == pygame.K_RIGHT:
            player_pos.left +=5

    if player_pos.left <0:
        player_pos.left = 0
    elif player_pos.right > SCREEN_WIDTH:
        player_pos.right = SCREEN_WIDTH

    # 적 내려오기
    for one in enemies:
        one.top += 5
        if one.bottom > SCREEN_HEIGHT:
            one.top = -100
            one.left = random.randint(0, SCREEN_WIDTH-enemy_img.get_width())

    # 이미지 그리기
    screen.blit(player_img, player_pos)

    for one in enemies:
        screen.blit(enemy_img, one)
    pygame.display.flip()

    clock.tick(120)