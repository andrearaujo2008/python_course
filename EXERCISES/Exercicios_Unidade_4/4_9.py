
qtd = 0

while qtd < 9:
    numero = input("Insira o numero do nif: ")
    # numero = (r"\d{3}.\d{3}.\d{3}")
    qtde_num = len(numero)

    if qtde_num < 9:
        print("Numero do nif digitado nao esta correto, por digite novamente!")


print(f"Numero do nif correto {numero}")
