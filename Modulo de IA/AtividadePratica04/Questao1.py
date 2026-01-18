"""
1 - Criar um código que faça uma calculadora que tenha as operações básicas(+,-,*,/).
"""

try:
    def soma(a,b):
        resultado = a + b
        return resultado

    def subtracao(a,b):
        resultado = a - b
        return resultado

    multiplicacao = lambda a,b: a* b
    divisao = lambda a, b: a/b
    total = 0

    valor1 = float(input("Digite o primeiro valor: "))
    valor2 = float(input("Digite o segundo valor: "))
    operacao = input("Escolha a operação desejada: \n+ para somar \n- para subtrair\n* para multiplicar \n/ para dividir\nQual operação deseja realizar? ")
    if operacao == '+':
        total = soma(valor1, valor2)
    elif operacao == '-':
     total = subtracao(valor1, valor2)
    elif operacao == '*':
        total = multiplicacao(valor1, valor2)
    elif operacao == '/':
        total = divisao(valor1, valor2)
    else:
        print("Opção inválida")
        exit()
    print(f"Valor 1: {valor1:.2f}",f"\nValor 2: {valor2:.2f}","\nOperação realizada",operacao ,f"\nResultado: {total:.2f}")
except ZeroDivisionError:
    print("Valor não pode ser divisível por zero")
except ValueError:
    print("O valor a ser digitado deve ser numérico")