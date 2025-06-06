import requests

id_personagem = input("Digite o id do personagem: ")

response = requests.get(f"http://ponyapi.net/v1/character/{id_personagem}")

personagem_json = response.json()

nome_personagem = personagem_json["data"][0]["name"]

print(nome_personagem)