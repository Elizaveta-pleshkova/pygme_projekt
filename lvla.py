import pygame

koord = {1: (60,60), 2: (300, 180), 3: (180, 420), 4: (300, 540)}
class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 10
        self.top = 10
        self.cell_size = 120

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self):
        for y in range(self.height):
            for x in range(self.width):
                pygame.draw.rect(screen, (0, 0, 0), (x * self.cell_size, y * self.cell_size,
                                                                 self.cell_size, self.cell_size), 5)

class Urovni:
    def __init__(self, lvl=0):
        self.lvl = lvl

    def moving(self):
        k = koord.get(self.lvl)
        self.x = k[0]
        self.y = k[1]

        pygame.draw.circle(screen, (250, 250, 250), (self.x, height - self.y), 50)


def decoration():
    imagefon = pygame.image.load('data/fon.jpg').convert_alpha()
    imagefon = pygame.transform.scale(imagefon, (800, 900))
    imagefon_top = screen.get_height() - imagefon.get_height()
    imagefon_left = screen.get_width() / 2 - imagefon.get_width() / 2
    screen.blit(imagefon, (imagefon_left, imagefon_top))
    image = pygame.image.load('data/planet.png').convert_alpha()
    image = pygame.transform.scale(image, (180, 180))
    image_rect = image.get_rect(bottomright=(150, 620))
    screen.blit(image, image_rect)
    image2 = pygame.image.load('data/planet2.png').convert_alpha()
    image2 = pygame.transform.scale(image2, (150, 150))
    image2_rect = image2.get_rect(bottomright=(370, 490))
    screen.blit(image2, image2_rect)
    image3 = pygame.image.load('data/planet3.png').convert_alpha()
    image3 = pygame.transform.scale(image3, (360, 190))
    image3_rect = image3.get_rect(bottomright=(380, 275))
    screen.blit(image3, image3_rect)
    image4 = pygame.image.load('data/planet4.png').convert_alpha()
    image4 = pygame.transform.scale(image4, (180, 180))
    image4_rect = image4.get_rect(bottomright=(385, 145))
    screen.blit(image4, image4_rect)




pygame.init()
size = width, height = 500, 600
screen = pygame.display.set_mode(size)
board = Board(4, 5)
pers = Urovni(1)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    board.render()
    decoration()
    pers.moving()
    pygame.display.flip()