"""
1- Crie um programa que escreve dados de pessoas (nome, idade e cidade) em um arquivo CSV.
Para isso:

 * Crie uma lista de listas com dados fictícios de pelo menos três pessoas.
 * Solicite ao usuário o nome do arquivo CSV onde os dados serão salvos.
 * Escreva os dados usando o módulo `csv`, com cabeçalhos apropriados.
 * Confirme a gravação exibindo uma mensagem com o nome do arquivo.
 * Trate possíveis erros de escrita de arquivo.

 Dica: Use `csv.writer()` para escrever os dados linha por linha.
"""


import csv

pessoas = [
    ["Ana", 22, "Cuiabá"],
    ["Carlos", 30, "São Paulo"],
    ["Marina", 27, "Rio de Janeiro"]
]

nomeArquivo = input("Digite o nome do arquivo CSV, coloque csv como extensão no final: ")

try:
    with open(nomeArquivo, mode="w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(["Nome", "Idade", "Cidade"])
        for pessoa in pessoas:
            escritor.writerow(pessoa)

    print(f"Arquivo '{nomeArquivo}' gravado com sucesso!")

except IOError:
    print("Erro ao escrever o arquivo. Verifique permissões ou o nome do arquivo.")
