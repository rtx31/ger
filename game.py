
import pygame
import sys

pygame.init()
WIDTH, HEIGHT = 800, 600
BG_COLOR = (30, 30, 30)
SPEED = 5

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Logo Game")

logo = pygame.image.load("logo.png").convert_alpha()
logo = pygame.transform.scale(logo, (80, 80))

player_x, player_y = WIDTH // 2, HEIGHT // 2

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]: player_x -= SPEED
    if keys[pygame.K_RIGHT]: player_x += SPEED
    if keys[pygame.K_UP]: player_y -= SPEED
    if keys[pygame.K_DOWN]: player_y += SPEED

    screen.fill(BG_COLOR)
    screen.blit(logo, (player_x, player_y))
    pygame.display.flip()
    clock.tick(60)
