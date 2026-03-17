# Listar aplicação tanto filter e map

numeros = [1, 4, 7, 10, 13, 16]

# Ver a lista de numeros pares
pares = list(filter(lambda x: x % 2 == 0, numeros))
# Somar os resultados da saida da função pares
somar = list(map(lambda x: x + 5, pares))

print(pares)  # Saida dos numeros Pares [4, 10, 16]

print(somar)  # Saida dos numeros somar [9, 15, 21]
