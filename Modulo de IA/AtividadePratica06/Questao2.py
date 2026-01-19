"""
2 -   Crie um programa que  acesse a API  para buscar um usuário fictício aleatório.
 exibindo o nome, e-mail e país desse usuário, caso houver erro na conexão, mostre uma mensagem de falha.
"""

import requests

try:
  
    response = requests.get("https://randomuser.me/api/")
    response.raise_for_status()  

    dados = response.json()
    usuario = dados["results"][0]

    nome = usuario["name"]["first"] + " " + usuario["name"]["last"]
    email = usuario["email"]
    pais = usuario["location"]["country"]

    print("Usuário encontrado: ","\nNome:", nome, "\nE-mail:", email, "\nPaís:", pais)
except requests.exceptions.RequestException:
    print("Erro ao consultar a API")

