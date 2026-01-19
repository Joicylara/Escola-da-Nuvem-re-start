"""
3 - Crie um programa que consulte informações de um  na API , retorne logradouro, 
bairro, cidade e estado do CEP digitado, caso o CEP não existir ou houver erro na requisição, mostre uma mensagem de falha.
"""

import requests

cep = input("Digite somente os números do CEP: ").strip()

try:
    url = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url, timeout=5)
    response.raise_for_status()

    dados = response.json()

    if dados.get("erro"):
        print("CEP não encontrado.")
    else:
        logradouro = dados.get("logradouro", "Não informado")
        bairro = dados.get("bairro", "Não informado")
        cidade = dados.get("localidade", "Não informado")
        estado = dados.get("uf", "Não informado")

        print("\nEndereço encontrado:","\nLogradouro:", logradouro,"\nBairro:", bairro,"\nCidade:", cidade, "\nEstado:", estado)
except requests.exceptions.RequestException:
    print("Falha ao conectar com a API")

