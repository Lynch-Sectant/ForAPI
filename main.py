import pygame
import requsts


api_server = "http://static-maps.yandex.ru/1.x/"
params = {
    "ll": ",".join([0, 0]),
    "spn": ",".join([90, 90]),
    "l": "map"}
response = requests.get(api_server, params=params)
def load_image(name, colorkey=None):
    fullname = (name)
    # если файл не существует, то выходим
    image = pygame.image.load(fullname)
    return image


pygame.init()
size = width, height = 1000, 1000
screen = pygame.display.set_mode(size)
playing = True

while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pass
