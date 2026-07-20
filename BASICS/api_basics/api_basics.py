import requests

url = "https://pokeapi.co"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    pokemon_name = data["name"].capitalize()
    pokedex_id = data["id"]

    print("Bridge connection successful!")
    print(f"Name: {pokemon_name}")
    print(f"ID: {pokedex_id}")

else:
    print("Failed to connect to the API.")