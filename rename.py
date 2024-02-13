import os
import requests

def get_pokemon_name(pokemon_number):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_number}")
    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data["name"]
    else:
        return f"pokemon_{pokemon_number}"

directory = "Data/"

for filename in os.listdir(directory):
    if filename.endswith(".png"):
        parts = filename.split(".")[0].split("_")
        if len(parts) == 2 and parts[0] == "pokemon":
            try:
                pokemon_number = int(parts[1])
            except ValueError:
                continue 
        else:
            continue
    

        pokemon_name = get_pokemon_name(pokemon_number)
        old_path = os.path.join(directory, filename)
        new_path = os.path.join(directory, f"{pokemon_name}.png")
        os.rename(old_path, new_path)

        print(f"Renamed {filename} to {pokemon_name}.png")

print("All images renamed successfully!")
