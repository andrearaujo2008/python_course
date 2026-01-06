# Program will display 5 words per line

frase = input("Insert at least 5 words: ")
palavras = frase.split()
qtd = len(palavras)

print(f"A quantidade de palavras e: {qtd}")
