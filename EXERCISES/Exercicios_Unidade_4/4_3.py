# Calcular o cosseno, seno e tangente de um angulo
# Feito por Andre de Araujo 30/12/2025

import math

# Solicita ao usurio o angulo no qual será medido
angulo = int(input("Informe o numero do angulo: "))

# Converte o angulo em radianos
radianos = math.radians(angulo)

# Calcula o seno, cosseno e tangente do ângulo
coss = math.cos(radianos)
sen = math.sin(radianos)
tang = math.tan(radianos)

# imprime os resultados
print(f"O seno de {angulo} e {sen}")
print(f"O cosseno de {angulo} e {coss}")
print(f"O tangente de {angulo} e {tang}")
