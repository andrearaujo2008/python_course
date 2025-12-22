# Media de numeros digitados pelo usuario

num = int(input("Digite o numero: "))

# Coloca o contadores
soma = 0  # Para guardar os numeros positivos digitados
contador = 0  # Para guardar as vezes de loops que ira fazer ate que o numero seja negativo

# Condicao
while num > 0:
    soma += num  # Guarda o numero digitado
    contador += 1
    num = int(input("Digite outro numero: "))
else:
    # A media de valores que foi digitado ate que o numero foi negativo
    resultado = soma / contador
    print(f"A soma da media de numeros positivos digitados sera {resultado} ")
