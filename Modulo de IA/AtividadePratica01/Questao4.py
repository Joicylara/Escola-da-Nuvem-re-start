"""
4- Calculadora de Preço Total
* Desenvolva um programa que calcula o preço total de uma compra. Use as seguintes informações:

* Nome do produto: "Cadeira Infantil"
* Preço unitário: R$ 12.40
* Quantidade: 3
O programa deve calcular o preço total e exibir todas as informações, incluindo o resultado final.
"""
nomeProduto = "Cadeira Infantil"
precoUnitario = 12.40
quatidade = 3

total = precoUnitario*quatidade

print("Nome do produto:", nomeProduto, f"\nPreço unitário: {precoUnitario:.2f} " f"\nValor total: {total:.2f}")