import pygame

WIDTH = 360
HEIGHT = 480
FPS = 15

BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

class Square(pygame.sprite.Sprite):
    x = 50
    y = 50

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((56, 56))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)

    def update(self):
        if self.x > 0:
            if self.y > 0:
                self.x -= 2
                self.y -= 2
                self.image = pygame.Surface((self.x, self.y))
                self.image.fill(YELLOW)
                self.rect = self.image.get_rect()
                self.rect.center = (WIDTH / 2, HEIGHT / 2)
        else:
            self.x = 56
            self.y = 56


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

    screen.fill(BLUE)
    all_sprites.draw(screen)

    all_sprites.update()

    pygame.display.flip()

pygame.quit()
