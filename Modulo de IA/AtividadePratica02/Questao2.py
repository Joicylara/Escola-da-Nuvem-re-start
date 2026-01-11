"""
2- Calculadora de Desconto
Desenvolva um programa que calcula o desconto em uma loja. Use as seguintes informações:

* Nome do produto: "Camiseta"
* Preço original: R$ 50.00
* Porcentagem de desconto: 20%
O programa deve calcular o valor do desconto e o preço final, exibindo todos os detalhes.
"""

nomeProduto = "Camiseta"
precoOrginal= 50.00
porcentagemDesconto = 20

valorComDesconto = precoOrginal - (precoOrginal * porcentagemDesconto / 100)

print("Nome produto: ",nomeProduto, f"\nValor do produto: {precoOrginal:.2f}", "\nDesconto: ", porcentagemDesconto, "%", f"\nValor com desconto aplicado: {valorComDesconto:.2f}")


# Com entrada de dados
nomeDoProduto = str(input("Digite o nome do produto: "))
precoProduto = float(input("Digite o preço do produto: "))

desconto = 20
valorDesconto = precoProduto - (precoProduto * desconto / 100)

print("Nome produto: ",nomeDoProduto, f"\nValor do produto: {precoProduto:.2f}", "\nDesconto: ", desconto, "%", f"\nValor com desconto aplicado: {valorDesconto:.2f}")

