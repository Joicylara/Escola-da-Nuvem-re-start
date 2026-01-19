"""
1 - Crie um programa que gere senhas aleatórias com letras, 
números e símbolos e que o usuário  também escolha o tamanho da senha  para criar senhas seguras automaticamente.
"""

import requests

def gerarSenha(tamanho: int) -> str:
    url = f"https://randomuser.me/api/?password=upper,lower,number,special,{tamanho}-{tamanho}"
    
    response = requests.get(url)
    dados = response.json()
    
    senha = dados['results'][0]['login']['password']
    return senha

try:
    tamanho = int(input("Digite o tamanho da senha: "))

    if tamanho <= 0:
        print("O tamanho deve ser maior que zero.")
    else:
        senha = gerarSenha(tamanho)
        print("Senha gerada:", senha)

except ValueError:
    print("Digite um número válido.")
