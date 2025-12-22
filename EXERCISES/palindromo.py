# Este programa verifica se a palavra e digitada e palindromo ou nao

palavra = input("Digite a palavra: ")
inverso = palavra[::-1]

# Condicao para saber se a palavra sera polindromo ou nao
if inverso == palavra:
    print('Esta palavra e polindromo')
else:
    print('Esta palavra nao e polindromo')
