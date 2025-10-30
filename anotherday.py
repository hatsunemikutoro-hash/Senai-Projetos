
import pygame

pygame.init()

# configurações
w, h = 800,600
window = pygame.display.set_mode((w,h))
running = True
clock = pygame.time.Clock()

# player
player_surf = pygame.Surface((30,30))
player_surf.fill("black")
player_rect = player_surf.get_frect(center=(w - 700, h / 2))

# cano
pipe_surf = pygame.Surface((100,500))
pipe_surf.fill("green")
pipe_rect = pipe_surf.get_frect(center=(100,100))

# variaveis
y_spd = 0
jump_p = -350
grv = 800
spd = 200

# loop principal
while running:
    dt = clock.tick(60) / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    y_spd += grv * dt


    keys = pygame.key.get_just_pressed()
    if keys[pygame.K_SPACE]:
        y_spd = jump_p

    window.fill("white")
    pipe_rect.centerx -= 200 * dt
    player_rect.y += y_spd * dt
    window.blit(player_surf, player_rect)

    pygame.display.update()
pygame.quit()