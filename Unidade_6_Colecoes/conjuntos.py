# Conjunto de numeros

numeros1 = {1, 2, 3, 4, 5}
numeros2 = {3, 4, 5, 6, 7}

conjunto1 = set(numeros1)
conjunto2 = set(numeros2)

uniao = conjunto1.union(conjunto2)  # Aqui vai reunir os dois numeros

intersecao = conjunto1.intersection(conjunto2)  # Só vai separar os numeros que bater com conjunto1

diferenca = conjunto1.difference(conjunto2)  # Só vai mostrar os numeros que não pertence ao conjunto 2

print(conjunto1)

print(uniao)

print(intersecao)

print(diferenca)
