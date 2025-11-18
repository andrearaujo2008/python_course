# Este programa ira dizer quantos dias o remedio dura para um determinado paciente

# Informaçao do produto
nome = input("Digite o nome do remedio: ").lower()
quant1 = int(input("Digite a quantidade total do remedio: "))
quant2 = float(input("Digite a quantidade que toma no dia: "))

# Soma da quantidade do remedio com a quantidade que toma por dia
dias = int(quant1 / quant2)

# Resultado de quantos dias o produto dura
print(f"O remedio {nome} ira durar: {dias} dias")
