# This programm will check if a old man if time to retire or not

nome = input("Digite o seu nome: ")
idade = int(input("Digite a idade do cliente: "))
gen = input("Digite M ou F: ").upper()[0]

if (gen != "M") and (gen != "F"):
    print("Este genero nao existe, por favor digite novamente")

elif (gen == "M" and idade >= 65) or (gen == "F" and idade >= 60):
    print(f"{nome} tem direito a aposentadoria")
else:
    print(f"{nome} nao tem direito a aposentadoria")
