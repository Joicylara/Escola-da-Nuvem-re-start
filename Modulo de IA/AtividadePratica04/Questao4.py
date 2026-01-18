"""
4 - Criar um código que serve para analisar números digitados pelo usuário, classificando-os como pares ou ímpares e contabilizando quantos de cada tipo foram inseridos.
"""

pares = 0
impares = 0

while True:
    entrada = input("Digite um número inteiro ou 'fim' para encerrar: ").lower()

    if entrada == 'fim':
        break

    try:
        numero = int(entrada)

        if numero % 2 == 0:
            print(f"{numero} é par")
            pares = pares + 1
        else:
            print(f"{numero} é ímpar")
            impares = impares + 1

    except ValueError:
        print("Digite um número inteiro válido.")

print("\nResultado final:",f"\nQuantidade de números pares: {pares}", f"\nQuantidade de números ímpares: {impares}")

