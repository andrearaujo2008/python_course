# Verificacao Idade
idade = int(input("Digite a tua idade: "))
if idade < 18:
    print("Voce e menor de idade")
elif idade >= 18 and idade < 60:
    print("Voce e maior de idade. ")
else:
    print("Voce e idoso")
