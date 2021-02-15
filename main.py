import pygame
import requests


def load_image(name, colorkey=None):
    fullname = (name)
    # если файл не существует, то выходим
    image = pygame.image.load(fullname)
    return image


scale = 90
api_server = "http://static-maps.yandex.ru/1.x/"
params = {
    "ll": ",".join(['0', '0']),
    "spn": ",".join([f'{scale}', f'{scale}']),
    "l": "map"}
response = requests.get(api_server, params=params)
pygame.init()
size = width, height = 1500, 1000
screen = pygame.display.set_mode(size)
running = True
with open("map.png", "wb") as file:
    file.write(response.content)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_PAGEUP:
                if scale != 90:
                    scale += 10
            if event.key == pygame.K_PAGEDOWN:
                if scale != 0:
                    scale -= 10
            params["spn"] = ",".join([f'{scale}', f'{scale}'])
            response = requests.get(api_server, params=params)
            pygame.init()
            size = width, height = 1500, 1000
            screen = pygame.display.set_mode(size)
            running = True
            with open("map.png", "wb") as file:
                file.write(response.content)
        fon = pygame.transform.scale(load_image('map.png'), (1500, 1000))
        screen.blit(fon, (0, 0))
    pygame.display.flip()
pygame.quit()
