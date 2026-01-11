"""
4- Calculadora de Consumo de Combustível
Desenvolva um programa que calcula o consumo médio de combustível de um veículo. Use os seguintes dados:

* Distância percorrida: 300 km
* Combustível gasto: 25 litros
O programa deve calcular o consumo médio (km/l) e exibir todos os dados da viagem, incluindo o resultado final arredondado para duas casas decimais.
"""

distanciaPercorrida = 300
combustivelGasto = 25

consumoMedio = distanciaPercorrida / combustivelGasto
print("Valor da distância percorrida: ", distanciaPercorrida, "km", "\nCombustível gasto: ", combustivelGasto, "L", f"\nConsumo médio: {consumoMedio:.2f}")

# Com entrada de dados

distancia = float(input("Digite a distância percorrida: "))
combustivelConsumido = float(input("Digite o combustível consumido: "))

consumoMedioLitroQuilometro = distancia / combustivelConsumido
print("Valor da distância percorrida: ", distancia, "km", "\nCombustível gasto: ", combustivelConsumido, "L", f"\nConsumo médio: {consumoMedioLitroQuilometro:.2f}")
