"""
 2- Desenvolva um programa que lê os dados de um arquivo CSV e imprime cada linha na tela.
Para isso:

 * Solicite ao usuário o nome do arquivo CSV a ser lido.
 * Utilize o módulo `csv` para abrir o arquivo e ler os dados.
 * Exiba cada linha completa como uma lista.
 * Trate erros como arquivo inexistente ou problemas na leitura.

 Dica: Use `csv.reader()` para ler e percorrer as linhas do arquivo.

"""

import csv

nomeArquivo = input("Digite o nome do arquivo CSV a ser lido não esqueça a extensão csv: ")

try:
    with open(nomeArquivo, mode="r", encoding="utf-8") as arquivo:
        leitor = csv.reader(arquivo)

        print("\nConteúdo do arquivo:")
        for linha in leitor:
            print(linha)

except FileNotFoundError:
    print("Erro: Arquivo não encontrado.")
except IOError:
    print("Erro ao ler o arquivo.")
