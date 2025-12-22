# Este programa você devera saber se o numero que o programa gerou e maior ou menor do numero que você digitou

# Autor: Andre de Araujo
# Data: 28/11/2025

# importando a biblioteca random
import random

# Gerando um numero aleatorio de 1 a 10
ran = random.randint(1, 10)

num = int(input("Digite um numero de 1 a 10: "))

# Condicao se o numero digitado e maior, menor ou igual do numero gerado no sistema
if num > ran:
    print(f"O numero {num} e maior do que numero gerado no sistema {ran}")
elif num < ran:
    print(f"O numero {num} e menor do que numero gerado no sistema {ran}")
else:
    print(f"O numero {num} e mesmo que numero gerado no sistema {ran}")
