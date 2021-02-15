import pygame


pygame.init()
size = width, height = 1000, 1000
screen = pygame.display.set_mode(size)
playing = True

while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        else:
            pass
