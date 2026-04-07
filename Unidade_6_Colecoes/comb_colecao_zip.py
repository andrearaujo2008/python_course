# Usando combinações de coleções

nomes = ["Joao", "Jose", "Maria", "Pedro"]
idades = [25, 30, 20]
pessoas = zip(nomes, idades)
for nomes, idades in pessoas:
    print(f"{nomes} tem {idades}anos")
