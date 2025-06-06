import requests

nome_personagem = input("Digite o nome do personagem: ")

response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{nome_personagem}")

personagem_json = response.json()

habilidade_personagem = personagem_json["abilities"][0]["ability"]["name"]



for i in range (0,2):
    print(personagem_json["abilities"][i]["ability"]["name"])
    i+=1
