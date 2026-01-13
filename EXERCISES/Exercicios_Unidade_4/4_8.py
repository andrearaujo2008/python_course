# Program will display 5 words per line

import re

qtd = 0

while qtd < 5:

    # Here you insert the phrase
    frase = input("Insert at least 5 words: ")

    palavras = frase.split()  # Here the words will be separated

    qtd = len(palavras)  # Count how many words exist on the phrase

    if qtd < 5:  # Conditional if words have less than 5

        print("Your phrase must have at least 5 words. Please write again!")

# Case the words is more 5 words it will separate each line
resultado = re.sub(r"\s+", "\n", frase)

# Display the phrase
print(resultado)
