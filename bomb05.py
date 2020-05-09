# 폭탄 피하기

import pygame
import random

# 변수 설정
WHITE = (255,255,255)
BLACK = (0,0,0)
YELLOW = (255,255,0)
GRAY = (240,240,240)
PURPLE = (133,0,255)

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

# 변수 초기화
score = 0
enemy_num = 5
gameover = False

# 파이게임 초기화
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Bomb Game : minseok")
frame = pygame.time.Clock()
pygame.key.set_repeat(1)

small_font = pygame.font.SysFont("Agency F8", 30)
large_font = pygame.font.SysFont("", 72)

player_url = 'resources/images/people.png'
player_img = pygame.image.load(player_url)
player_pos = player_img.get_rect(centerx = SCREEN_WIDTH // 2,
                                 bottom = SCREEN_HEIGHT)

enemy_url = 'resources/d_images/virus.png'
enemy_img = pygame.image.load(enemy_url)
# enemies info는 적의 좌표와 속도를 리스트로 저장
enemies_info = []
for cnt in range(enemy_num):
    enemy_pos = enemy_img.get_rect(left = random.randint(0,SCREEN_WIDTH-enemy_img.get_width()),
                                   bottom = -100 * cnt)
    enemy_speed = random.randint(5,15)
    enemies_info.append([enemy_pos,enemy_speed])

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()
        if not gameover and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_pos.left -= 5
            elif event.key == pygame.K_RIGHT:
                player_pos.left += 5

    if player_pos.left < 0:
        player_pos.left = 0
    elif player_pos.right > SCREEN_WIDTH:
        player_pos.right = SCREEN_WIDTH

    if not gameover:
        for one in enemies_info:
            #one: [ (1,0),5 ]
            one[0].top += one[1]
            if one[0].top > 800:
                one[0].left = random.randint(0, SCREEN_WIDTH-enemy_img.get_width())
                one[0].top = -100
                one[1] = random.randint(5,15)
                score += 1
                if (score % 20 ==0):
                    enemy_pos = enemy_img.get_rect(left=random.randint(0, SCREEN_WIDTH - enemy_img.get_width()),
                                                   bottom=-100 * cnt)
                    enemy_speed = random.randint(5, 15)
                    enemies_info.append([enemy_pos, enemy_speed])

    # 적 충돌 처리
    for one in enemies_info:
        # one: [ (1,0),5 ]
        if one[0].colliderect(player_pos):
            gameover = True


    screen.fill(GRAY)
    screen.blit(player_img, player_pos)
    for one in enemies_info:
        # one: [ (1,0),5 ]
        screen.blit(enemy_img, one[0])

    # 점수 출력
    score_img = small_font.render("SCORE:{}".format(score),True,PURPLE)
    screen.blit(score_img, (10,10))

    # 게임 종료
    if gameover:
        gameover_img = large_font.render("GameOver", True, PURPLE)
        screen.blit(gameover_img,(SCREEN_WIDTH // 2-gameover_img.get_width() //2,
                                  SCREEN_WIDTH // 2- gameover_img.get_height()//2))

    pygame.display.flip()
    frame.tick(60)



