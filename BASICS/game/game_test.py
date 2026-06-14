import pygame
pygame.init()

screen = pygame.display.set_mode((700, 500))

running = True

font = pygame.font.SysFont("arial", 30)

while running:

    text = font.render('Hi Game', True, (255, 255, 255))

    text_rect = text.get_rect()
    text_rect.center = (700 //2, 500 //2)

    screen.blit(text, text_rect)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.flip()

pygame.quit()