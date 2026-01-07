# Program will display 5 words per line

qtd = 0

while qtd < 5:

    # Here you insert the phrase
    frase = input("Insert at least 5 words: ")

    palavras = frase.split()  # Here the words will be separated

    qtd = len(palavras)  # Count how many words exist on the phrase

    if qtd < 5:

        print("Your phrase must have at least 5 words. Please write again!")

print(f"A quantidade de palavras e: {qtd}")
