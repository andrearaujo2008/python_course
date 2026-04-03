
numeros = [1, 2, 3, 2, -5, 4, 3, 1, -2]

quadrados_unicos = {x**2 for x in numeros if x > 0}

print(quadrados_unicos)  # Saida {16, 1, 4, 9}
