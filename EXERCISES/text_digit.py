# Programa para saber se texto digitado e numero ou string

texto = str(input("Digite qualquer coisa: "))

if texto.isdigit():
    print("Este texto é um número inteiro.")
else:
    print("Este texto contém caracteres não-numéricos ou está vazio.")
