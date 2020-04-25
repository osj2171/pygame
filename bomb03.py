# 플레이어 이동

import pygame

WHITE = (255,255,255)
BLACK = (0,0,0)

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()

# 키 반복
pygame.key.set_repeat(1)

# 이미지 불러오기
#화면 중앙 하단배치: centerx, bottom 속성 사용하기
player_url = 'resources/d_images/people.png'
player_img = pygame.image.load(player_url)
player_pos = player_img.get_rect(centerx = SCREEN_WIDTH//2,
                                 bottom = SCREEN_HEIGHT)

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
        # 벽 충돌 처리
    if player_pos.left <0:
        player_pos.left = 0
    elif player_pos.right > SCREEN_WIDTH:
        player_pos.right = SCREEN_WIDTH

    screen.blit(player_img, player_pos)
    pygame.display.flip()

    # 프레임 설정
    clock.tick(120)




