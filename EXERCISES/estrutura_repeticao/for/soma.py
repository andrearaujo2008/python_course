# Programa que soma todos os numeros pares a partir de 1 ate o N digitado pelo usuario
# Desenvolvido por: Andre de Araujo
# Data 03/12/2025

# Entrada do numero que será somado
n = int(input("Digite o numero: "))
soma = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        soma += i
        print(f"A soma dos numeros pares de 1 ate {n} e: {soma}")
