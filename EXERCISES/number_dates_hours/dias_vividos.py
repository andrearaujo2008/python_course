# Este programa ira mostrar quantos dias você tem desde que você nasceu

import datetime

dataNascimento_str = input("Digite a data do seu nascimento (DD/MM/AAAA): ")
dataNascimento = datetime.datetime.strptime(dataNascimento_str, "%d/%m/%Y")
dataAtual = datetime.datetime.now()
diferenca = dataAtual - dataNascimento

print(f"Voce ja viveu {diferenca.days} dias.")
