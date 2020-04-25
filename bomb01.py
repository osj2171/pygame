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

while True:
    screen.fill(WHITE)

    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        exit()

    screen.blit(player_img, (100,100))

    pygame.display.flip()