"""
 3- Desenvolva um programa que cria um dicionário com dados de uma pessoa e salva esses dados em um arquivo JSON.
Em seguida, o programa deve ler o mesmo arquivo e exibir o conteúdo.
Para isso:

 * Crie um dicionário com pelo menos três campos (ex: nome, idade, cidade).
 * Solicite ao usuário o nome do arquivo JSON.
* Salve os dados no arquivo usando o módulo `json`.
 * Após salvar, leia o mesmo arquivo e imprima os dados carregados.
 * Trate possíveis erros como ausência do arquivo ou problemas na escrita.

 Dica: Use `json.dump()` para escrever e `json.load()` para ler o arquivo.
"""

import json


pessoa = {
    "nome": "Ana Souza",
    "idade": 28,
    "cidade": "Cuiabá"
}
nomeArquivo = input("Digite o nome do arquivo JSON, use a extensão json no final: ")

try:
    with open(nomeArquivo, "w", encoding="utf-8") as arquivo:
        json.dump(pessoa, arquivo, ensure_ascii=False, indent=4)
    
    print(f"Dados gravados com sucesso no arquivo '{nomeArquivo}'.")

except IOError:
    print("Erro ao escrever no arquivo.")

try:
    with open(nomeArquivo, "r", encoding="utf-8") as arquivo:
        dadosLidos = json.load(arquivo)
    
    print("\nDados lidos do arquivo:")
    print(dadosLidos)

except FileNotFoundError:
    print("Arquivo não encontrado.")
except json.JSONDecodeError:
    print("Erro ao ler o conteúdo do arquivo JSON.")
except IOError:
    print("Erro ao abrir o arquivo.")
