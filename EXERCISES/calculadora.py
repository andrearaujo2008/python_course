# Programa de calculadora em python

n1 = float(input("Digite o primeiro numero:"))
n2 = float(input("Digite o segundo numero: "))
operador = input("Digite o operador aritmetico: ")

match operador:
    case "+":
        resultado = n1 + n2
        print(f"O resultado e: {resultado}")
    case "-":
        resultado = n1 - n2
        print(f"O resultado e: {resultado}")
    case "*":
        resultado = n1 * n2
        print(f"O resultado e: {resultado}")
    case "/":
        if n2 == 0:
            print("Erro: divisao por zero!")
        else:
            resultado = n1 / n2
            print(f"O resultado e: {resultado}")
    case _:
        print("Operador invalido Use +, -, *, ou /.")
