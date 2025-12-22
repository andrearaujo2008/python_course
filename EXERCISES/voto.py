# Verificar se a pessoa e obrigado a vota ou nao

idade = int(input('Digite a idade: '))

if idade >= 18 and idade <= 70:
    print('Voce e obrigado a votar')
elif idade >= 16 and idade < 18 or idade > 70:
    print('Voce e apto a votar mas voce nao e obrigatorio')
else:
    print('Voce nao e apto a votar')
