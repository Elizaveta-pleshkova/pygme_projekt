import pygame

koord = {1: ('data/planet.png', (550, 550), (650, 420)),2: ('data/planet2.png', (550, 550), (650, 420)),
         3: ('data/planet3.png', (1100, 600), (1000, 450)), 4: ('data/planet4.png', (530, 530), (600, 370))}

def hero(name):
    image = pygame.image.load(name).convert_alpha()
    image = pygame.transform.scale(image, (600, 800))
    image_rect = image.get_rect(bottomright=(390, 835))
    screen.blit(image, image_rect)

def planet(name, kord, razmer):
    image = pygame.image.load(name).convert_alpha()
    image = pygame.transform.scale(image, kord)
    image_rect = image.get_rect(bottomright=razmer)
    screen.blit(image, image_rect)

def fon(name):
    imagefon = pygame.image.load(name).convert_alpha()
    imagefon = pygame.transform.scale(imagefon, (800, 900))
    imagefon_top = screen.get_height() - imagefon.get_height()
    imagefon_left = screen.get_width() / 2 - imagefon.get_width() / 2
    screen.blit(imagefon, (imagefon_left, imagefon_top))


def draw_txt():
    font = pygame.font.Font(None, 25)
    text = font.render("Нельзя поворачивать уже повернутую картинку.", 1, (100, 255, 100))
    text_x = 10
    text_y = height - 100
    screen.blit(text, (text_x, text_y))
    pygame.draw.rect(screen, (0, 255, 0), (0, height - 100,
                                           width, 100), 1)




pygame.init()
size = width, height = 500, 600
screen = pygame.display.set_mode(size)
screen.fill((0, 0, 0))
lvl = 3
forplanet = koord.get(lvl)
fon('data/fon.jpg')
planet(forplanet[0], forplanet[1], forplanet[2])
hero('data/hero4.png')
draw_txt()
pygame.display.flip()
while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()