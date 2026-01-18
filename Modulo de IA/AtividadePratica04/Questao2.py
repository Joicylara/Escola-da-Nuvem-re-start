"""
2 - Criar um código que registre as notas de alunos e calcular a média da turma.
"""
quantidade = 0
soma = 0

while True:
    entrada = input("Digite a nota, valores entre 0 a 10: ").lower()

    if entrada == 'fim':
        break
    try:

        nota = float(entrada)

        if 0 <= nota <=10:
            soma = soma + nota
            quantidade = quantidade + 1
        else:
            print("Nota inválida")
    except ValueError:
        print("A nota deve ser valor numérico")
if quantidade > 0:
    media = soma / quantidade
    print(f"A média da turma é: {media:.2f}")
else:
    print("Valor inválido")
