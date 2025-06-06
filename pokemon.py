import requests

#id_personagem = input("Digite o nome do personagem: ")

response = requests.get(f"https://pokeapi.co/api/v2/pokemon/squirtle")

personagem_json = response.json()

nome_personagem = personagem_json["abilities"][0]["ability"]["name"]

print(nome_personagem)