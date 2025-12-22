# Este programa o usuario vai digitar o numero do NIF (tipo cpf no brasil) para saber se e valido no territorio

# Autor: Andre de Araujo
# Data: 28/11/2025

nif = (input("Digite o numero do nif: "))

if len(nif) == 9 and nif.isdigit():
    print("O numero do NIF e valido!!!")
else:
    print("O numero NIF Invalido!!!")
