# Programa que valida se seu nif é valido ou nao

import re  # Libary to use regex
qtd = 0  # Initialize count

# Condition while if number to different 9
while qtd != 9:
    numero = input("Insira o numero do nif: ")

    qtd = len(numero)  # amount the numbers
# Condition if validade the number inserted by user is correct

# Standarlize the formatted using regex
standart = re.sub(r"(\d{3})(\d{3})(\d{3})", r"\1.\2.\3", numero)

# Resulting xxx.xxx.xxx
print(f"Seu Numero do nif esta correto: {standart}")
