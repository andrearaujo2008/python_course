# Exemplo 1 : Leitura de numeros positivos

num = int(input("Digite o numero: "))
# Enquanto o numero for maior que 0 ele irá executar
while num >= 0:
    print(f"Voce digitou o numero: {num}")

    num = int(input("Digite outro numero: "))
    # Aqui se digitar o numero negativo ele vai mostrar a informacao e depois ira encerrar o programa.
else:
    print("Voce digitou numero negativo")
