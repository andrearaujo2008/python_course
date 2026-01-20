
frase = input("Digite a frase: ")
# Cada 6 ele vai para outra linha
for i in range(0, len(frase), 6):
    # Resultado
    print(frase[i:i + 6])
