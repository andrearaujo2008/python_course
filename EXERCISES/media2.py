n1 = float(input('Digite o primeiro numero: '))
n2 = float(input('Digite o segundo numero: '))
n3 = float(input('Digite o terceiro numero: '))

soma = (n1 + n2 + n3) / 3

if soma >= 6 and soma <= 9.9:
    print(f"{soma:.2f} Aprovado!")
elif soma == 10:
    print(f'{soma:.2f} Parabens!')
else:
    print(f' {soma:.2f} Reprovado!')
