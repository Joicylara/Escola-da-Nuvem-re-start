"""
3- Calculadora de Média Escolar
Crie um programa que calcula a média escolar de um aluno. Use as seguintes notas:

* Nota 1: 7.5
* Nota 2: 8.0
* Nota 3: 6.5
O programa deve calcular a média e exibir todas as notas e o resultado final, arredondando para duas casas decimais.
"""

nota1 = 7.5
nota2 = 8.0
nota3 = 6.5

media = (nota1 + nota2 + nota3) / 3

print(f"Nota 1: {nota1:.2f}", f"\nNota 2: {nota2:.2f}", f"\nNota 3: {nota3:.2f}", f"\nMédia das notas: {media:.2f}")

# Com entrada de dados

primeiraNota = float(input("Digite a primeira nota: "))
segundaNota = float(input("Digite a segunda nota: "))
terceiraNota = float(input("Digite a terceira nota: "))

mediaNotas = (primeiraNota + segundaNota + terceiraNota) / 3

print(f"Nota 1: {primeiraNota:.2f}", f"\nNota 2: {segundaNota:.2f}", f"\nNota 3: {terceiraNota:.2f}", f"\nMédia das notas: {mediaNotas:.2f}")
