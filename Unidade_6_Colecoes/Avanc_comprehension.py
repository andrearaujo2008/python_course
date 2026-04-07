# Avancado comprehension

numeros = [1, 2, 3, 4, 5]
quadrados = [(x, x**2) for x in numeros if x < 4]
print(quadrados)  # Saida [(1, 1), (2, 4), (3, 9)]
