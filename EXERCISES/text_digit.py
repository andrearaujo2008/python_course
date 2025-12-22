# Programa para saber se texto digitado e numero ou string

texto = str(input("Digite qualquer coisa: "))

if texto.isdigit():  # Este comando ele vai dizer se o caracterer que voce digitou e um numero ou letra
    print("Este texto é um número inteiro.")
else:
    print("Este texto contém caracteres não-numéricos ou está vazio.")
