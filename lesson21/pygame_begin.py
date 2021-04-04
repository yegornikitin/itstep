import pygame

WIDTH = 360
HEIGHT = 480
FPS = 30

BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

class Square(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)


pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
yellow_square = Square()
all_sprites.add(yellow_square)


running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update()

    screen.fill(BLUE)
    all_sprites.draw(screen)

    pygame.display.flip()

pygame.quit()
