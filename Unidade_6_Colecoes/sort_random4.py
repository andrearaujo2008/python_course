import random

frutas = {1: "Banana", 2: "Morango", 3: "Uva"}
chaves = list(frutas.keys())
chave_aleatoria = random.choice(chaves)
print(chave_aleatoria)
