"""
4 - Crie um programa que calcule a quantos dias um individuo está vivo de acordo com a data do dia.
"""
from datetime import date

try:
    dia = int(input("Digite o dia de nascimento: "))
    mes = int(input("Digite o mes de nascimento: "))
    ano = int (input("Digite o ano de nascimento: "))
     
    dataNascimento = date(ano, mes, dia)
    dataHoje = date.today()

    if dataNascimento > dataHoje:
        print("Data de nascimento não pode ser no futuro")
    else:
        diasVivos = (dataHoje - dataNascimento).days
        print(f"Vivo há {diasVivos} dias")
except ValueError:
    print("Data inválida")