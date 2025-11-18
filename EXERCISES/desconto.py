# Price with discount

valor1 = float(input("Digite o valor do produto: "))
valor2 = int(input("Digite o valor de desconto: "))

desconto = valor2 / 100

resultado = valor1 * desconto
preco = valor1 - resultado

print(f'Valor do desconto sera: R$ {resultado} reais')
print(f'Preco final do produto sera: R$ {preco} reais')
