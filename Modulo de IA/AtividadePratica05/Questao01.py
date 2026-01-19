"""
1 - Crie uma função que calcule a gorjeta a ser deixada em um restaurante, baseada no valor total da conta e na porcentagem de
gorjeta desejada. Calcula o valor da gorjeta baseado no total da conta e na porcentagem desejada.
Parâmetros:
a - valor_conta (float): O valor total da conta
b - porcentagem_gorjeta (float): A porcentagem da gorjeta (ex: 10 para 10%)
c - retorna: float: O valor da gorjeta calculada
"""
try:
    def calcularGorjeta(conta, porcentagemGorjeta):
        gorjeta = conta * (porcentagemGorjeta/100)
        return gorjeta

    valor = float(input("Digite o valor total da conta: "))
    porcentagem = float(input("Digite a porcentagem da gorjeta: "))

    total = calcularGorjeta(valor,porcentagem)

    print(f"Valor da gorjeta: R$ {total:.2f}",f"\nValor total com gorjeta: R$ {valor + total:.2f}")
except ValueError:
    print("O valor deve ser numérico")