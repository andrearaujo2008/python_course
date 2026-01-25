frase = input("Digite a frase: ").strip()
# Cada 6 ele vai para outra linha
for i in range(len(frase)):
    if frase[i] != " " and (i == 0 or frase[i - 1] == " "):

        print(f"Palavra começa na posição: {i}")
