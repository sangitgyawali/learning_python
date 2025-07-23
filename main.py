# Request API Python

import requests

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)
    pokemon_data = response.json()
    print(pokemon_data)
    return pokemon_data

    if response.status.code == 200:
        print("Data retrieved!")
    else:
        print(f"'Failed to retrive data {response.status_code}")

pokemon_name = "pikachu"
pokemon_info = get_pokemon_info(pokemon_name)

if pokemon_info:
    print(f"{pokemon_info["name"]}")
    print(f"{pokemon_info["id"]}")
    print(f"{pokemon_info["height"]}")