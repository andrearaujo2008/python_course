# Use filter com lambda para criar uma lista apenas com as idades maiores ou iguais a 18.

idade = [12, 17, 18, 20, 15, 30]

permissao = list(filter(lambda x: x >= 18, idade))
print(permissao)
