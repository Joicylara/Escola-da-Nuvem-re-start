"""
3 - Crie um programa que serve para calcular o preço final de um produto após aplicar um desconto percentual.
a - Cálculo de desconto: Calcula o valor do desconto baseado em uma porcentagem.
b - Preço final: Determina o novo preço após o desconto.
c - Formatação: Arredonda o resultado para 2 casas decimais (centavos).
d - Interação com usuário: Pede os valores necessários e mostra o resultado formatado.
"""

def calcularPrecoComDesconto(preco: float, percentualDesconto: float) -> float:
    desconto = preco * (percentualDesconto / 100)
    precoFinal = preco - desconto
    return round(precoFinal, 2)


try:
    preco = float(input("Digite o preço do produto: R$ "))
    percentual = float(input("Digite o percentual de desconto (%): "))

    if preco < 0 or percentual < 0:
        print("Valores não podem ser negativos.")
    else:
        precoFinal = calcularPrecoComDesconto(preco, percentual)
        print(f"Preço final com desconto: R$ {precoFinal:.2f}")

except ValueError:
    print("Digite apenas valores numéricos")
