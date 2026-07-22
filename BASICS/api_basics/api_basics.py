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

    return poke_name, poke_id, hp, attack, defense




poke_name, poke_id, hp, attack, defense = pokemon_data()



pygame.init()

screen = pygame.display.set_mode((700, 500))
pygame.display.set_caption("Pokemon Stats")

font = pygame.font.SysFont("arial", 30)

running = True

while running:

    title_text = font.render(f"{poke_name} (ID: {poke_id})", True, (255, 255, 255))
    hp_text = font.render(f"HP: {hp}", True, (255, 255, 255))
    attack_text = font.render(f"Attack: {attack}", True, (255, 255, 255))
    defense_text = font.render(f"Defense: {defense}", True, (255, 255, 255))
    
    screen.blit(title_text, (100, 80))
    screen.blit(hp_text, (100, 160)) 
    screen.blit(attack_text, (100, 220))
    screen.blit(defense_text, (100, 280))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
pygame.quit()
