# Programa se digitar uma letra de nota ele vai dar um classificacao

nota = input("Digite a sua nota(A, B, C, D ou E): ").lower().strip()

match nota:
    case "a":
        print("Excelente")
    case "b":
        print("Bom")
    case "c":
        print("Regular")
    case "d":
        print("Ruim")
    case "e" | "f":
        print("Reprovado")
    case _:
        print("Nota nao existe!!!")
