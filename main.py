import pygame
from game_animator import AnimatedCharacter

pygame.init()
window = pygame.display.set_mode((800, 600))
coin = AnimatedCharacter(x=400, y=300)
coin.load_master_sprite_sheet("img.png", frame_width=100, frame_height=100)
coin.add_animation_from_range("spin", 1, 7, speed=2)
coin.play_animation("spin")

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    coin.update()
    
    window.fill((0, 0, 0))
    window.blit(coin.image, coin.rect)
    pygame.display.flip()
    
    clock.tick(60)

pygame.quit()