# Tabuada de um determinado numero
# Desenvolvido por Andre de Araujo
# Data: 04/12/2025

numero = int(input("Digite um numero, por favor: "))

for i in range(1, 11):
    resultado = numero * i

    print(f"{numero} x {i} = {resultado}")
