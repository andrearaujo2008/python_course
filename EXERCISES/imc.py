# Program that mensuare IMC
peso = float(input("Type your weight: "))
altura = float(input("Type your height: "))

imc = peso / altura ** 2

if (imc > 40):
    print(f"Resultado is Obesidade Grau III: {imc:.2f} ")
elif (imc < 39.9 and imc > 35):
    print(f"Resultado is Obesidade Grau II: {imc:.2f} ")
elif (imc < 34.9 and imc > 30):
    print(f"Resultado is Obesidade Grau I: {imc:.2f} ")
elif (imc < 29.9 and imc > 25):
    print(f"Resultado is Pre Obesidade: {imc:.2f} ")
elif (imc < 24.9 and imc > 18.5):
    print(f"Resultado is Peso Normal: {imc:.2f} ")
else:
    print(f"Resultado is Baixo Peso: {imc:.2f} ")
