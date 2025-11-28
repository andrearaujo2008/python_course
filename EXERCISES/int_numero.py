# Programa que ira revelar se todos os numeros inteiros sao pares e caso tiver 1 numero impar ele sera avisado

nums = [int(input("Digite um numero inteiro: ")) for _ in range(5)]


pares = [n for n in nums if n % 2 == 0]
impar = [n for n in nums if n % 2 != 0]

if len(impar) == 0:
    print("Todos os numero sao numeros inteiros")
else:
    print(f"Ha um numero que nao e inteiro {impar}")
