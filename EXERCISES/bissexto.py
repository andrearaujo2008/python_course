# Programming to create bissexto year
ano = int(input('Digite o ano:'))
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print("O Ano e bissexto.")
else:
    print("O Ano nao e bissexto.")
