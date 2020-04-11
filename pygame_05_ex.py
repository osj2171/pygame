import pygame

width, height = 640,800
size = (width,height)
screen = pygame.display.set_mode(size)

bloom2 = pygame.image.load('resources/images/bloom2.png')
castle35 = pygame.image.load('resources/images/castle35.png')

while True:
    screen.fill((0,0,0))

    bloom2_width = bloom2.get_width()
    bloom2_height = bloom2.get_height()
    for y in range(height // bloom2_height +1):
        for x in range(width // bloom2_width +1):
            screen.blit(bloom2, (x*bloom2_width, y*bloom2_height))

    castle35_height = castle35.get_height()
    for y in range(height // castle35_height):
        screen.blit(castle35, (0,30 + y * castle35_height))

    screen.blit(bloom2, (0,0))

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
