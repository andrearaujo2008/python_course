# This programm sum sen, con and tang from angular
import math

angulo_graus = int(input("Type the angle number: "))

# Converte de graus para radianos
angulo_radianos = math.radians(angulo_graus)

# Calcula seno, cosseno e tangente
seno = math.sin(angulo_radianos)
cosseno = math.cos(angulo_radianos)
tangente = math.tan(angulo_radianos)

# Show the result with 4 digits
print(f"Seno de {angulo_graus}º = {seno:.4f}")
print(f"Cosseno de {angulo_graus}º = {cosseno:.4f}")
print(f"Tangente de {angulo_graus}º = {tangente:.4f}")
