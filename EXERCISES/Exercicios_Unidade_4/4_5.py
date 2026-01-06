# Programa que calcula o fatorial de um numero

import math  # Aqui preciso importar a biblioteca para usar modulo fatorial

# Aqui voce vai pedi ao usuario inserir um numero
num = int(input("Insira um numero: "))

# Calculando o fatorial do numero
resultado = math.factorial(num)

print(f"O resultado fatorial de {num} e {resultado} ")
