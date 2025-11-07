# Verificacao do horario de funcionamento
dias = input("Digite o dia da semana: ")
hora = int(input("Digite a hora atual: "))
if dias == 'sabado' or dias == 'domingo' or hora < 9 or hora >= 17:
    print("Loja Fechada. ")
else:
    print("Loja Aberta ")
