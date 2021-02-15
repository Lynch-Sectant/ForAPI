import pygame
import requsts


def load_image(name, colorkey=None):
    fullname = (name)
    # если файл не существует, то выходим
    image = pygame.image.load(fullname)
    return image


api_server = "http://static-maps.yandex.ru/1.x/"
params = {
    "ll": ",".join(['0', '0']),
    "spn": ",".join(['90', '90']),
    "l": "map"}
response = requests.get(api_server, params=params)
pygame.init()
size = width, height = 1000, 1000
screen = pygame.display.set_mode(size)
playing = True
with open("map.png", "wb") as file:
    file.write(response.content)
while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            fon = pygame.transform.scale(load_image('map.png'), (1000, 1000))
            screen.blit(fon, (0, 0))
