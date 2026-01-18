"""
3- Conversor de Temperatura
Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin.
O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.
"""


try:
    
    temperatura = float(input("Digite a temperatura: "))
    unidadeOrigem = str(input("Unidade de medida:\n - C para Celsius\n - F para Fahrenheit\n - K para Kelvin\n Qual é a unidade da temperatura digitada? ").upper())
    unidadeConvertida = str(input("Unidade de conversão:\n - C para Celsius\n - F para Fahrenheit\n - K para Kelvin\nQual unidade deseja converter a temperatura? ").upper())
    conversao = 0


    if unidadeOrigem == 'C' and unidadeConvertida == 'K':
        conversao = temperatura + 273.15        
    elif unidadeOrigem == 'K' and unidadeConvertida == 'C':
        conversao = temperatura - 273.15      
    elif unidadeOrigem == 'C' and unidadeConvertida == 'F' :
        conversao = temperatura * 1.8 + 32      
    elif unidadeOrigem == 'F' and unidadeConvertida == 'C' :
        conversao = (temperatura - 32) / 1.8       
    elif unidadeOrigem == 'K' and unidadeConvertida == 'F' :
        conversao = (temperatura - 273.15) * 1.8 + 32       
    elif unidadeOrigem == 'F' and unidadeConvertida == 'K' :
        conversao = (temperatura - 32) * 5/9 + 273.15
    else:
        print("Temperatura já esta na unidade desejada de conversão ou essa unidade não existe")
        exit()
    print("Conversão realizada:", f"\nTemperatura {temperatura:.2f}", unidadeOrigem,f"\nTemperatura convertido para {conversao:.2f}",unidadeConvertida)
except ValueError:
    print("O valor a ser digitado deve ser numérico")       