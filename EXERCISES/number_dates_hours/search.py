import re
texto = input("Digita uma palavra sobre python:")
busca = re.search("divertido", texto)
if busca:
    print("Padrao encontrado!")
else:
    print("Padrão nao encontrado!")
