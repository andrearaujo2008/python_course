# Valida se o cpf e valido ou nao

import re

number = input("Digite o NIF no formato 999.999.999: ")
padrao_nif = r'\d{3}\.\d{3}\.\d{3}'

if re.fullmatch(padrao_nif, number):
    print("NIF no formato correto")
else:
    print("NIF nao esta no formato correto!")
