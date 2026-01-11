"""
1- Conversor de Moeda
Crie um programa que converte um valor em reais para dólares e euros. Use os seguintes dados:

* Valor em reais: R$ 100.00
* Taxa do dólar: R$ 5.20
* Taxa do euro: R$ 6.15
O programa deve calcular e exibir os valores convertidos, arredondando para duas casas decimais.
"""

valorReal = 100.00
taxaDolar = 5.20
taxaEuro = 6.15

converterDolar = valorReal / taxaDolar
converterEuro = valorReal / taxaEuro

print(f"O valor em real: {valorReal:.2f}", f"\nValor convertido para dólar: {converterDolar:.2f}", f"\nValor convertido para euro: {converterEuro:.2f}")

# Com entrada de dados
real = float(input("Digite o valor em real: "))


taxaDoDolar = 5.37
taxaDoEuro = 6.25

converterRealParaDolar = real / taxaDoDolar
converterRealParaEuro = real / taxaDoEuro

print(f"O valor em real: {real:.2f}", f"\nValor convertido para dólar: {converterRealParaDolar:.2f}", f"\nValor convertido para euro: {converterRealParaEuro:.2f}")