import pygame
import requests
import sys

def pokemon_data():
    url = " https://pokeapi.co/api/v2/pokemon/ditto"
    response = requests.get(url)
    data = response.json() 

    poke_name = data['name'].capitalize()
    poke_id = data['id']

    hp = data["stats"][0]["base_stat"]
    attack = data["stats"][1]["base_stat"]
    defense = data["stats"][2]["base_stat"]



pygame.init()

screen = pygame.display.set_mode((700, 500))

pygame.display.set_caption("Pokemon Stats")

font = pygame.font.SysFont("arial", 30)

running = True

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
