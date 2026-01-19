"""
4 - Crie um programa que realize consultas a  em relação ao Real (BRL) usando a API mostre valor atual, máxima, 
mínima e data/hora da última atualização, caso a moeda não existir ou houver erro na requisição, retorne uma mensagem de erro.
"""

import requests
from datetime import datetime

moeda = input("Digite a moeda ex: USD, EUR, BTC: ").upper()

try:
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"
    response = requests.get(url)
    response.raise_for_status()

    dados = response.json()

    chave = f"{moeda}BRL"

    if chave not in dados:
        print("Moeda não encontrada.")
    else:
        info = dados[chave]

        valorAtual = info["bid"]
        maxima = info["high"]
        minima = info["low"]

        timestamp = int(info["timestamp"])
        dataHora = datetime.fromtimestamp(timestamp).strftime("%d/%m/%Y %H:%M:%S")

        print("\nCotação da moeda:", moeda,"\nValor atual (BRL):", valorAtual, "\nMáxima do dia:", maxima, "\nMínima do dia:", minima, "\nÚltima atualização:", dataHora),
except requests.exceptions.RequestException:
    print("Erro ao consultar a API")

