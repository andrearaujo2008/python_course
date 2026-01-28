
preco = float(input("Digite o valor do preco:"))
desconto = float(input("Digite o valor do desconto:"))
taxa = float(input("Digite o valor da taxa:"))


def calcular_preco_final(taxa, desconto, preco):
    preco_final = preco - (taxa + desconto)
    print(f"O valor total é {preco_final}")


calcular_preco_final(taxa, desconto, preco)
