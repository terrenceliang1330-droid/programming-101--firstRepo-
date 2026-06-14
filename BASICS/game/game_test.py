import pygame
pygame.init()

screen = pygame.display.set_mode((700, 500))

running = True

font = pygame.font.Font(None, 30)



while running:

    text = font.render('Hi Game', True, (255, 255, 255))
    screen.blit(text, (300, 200))

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.flip()

pygame.quit()