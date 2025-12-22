# PROGRAMA DE VESTIMENTO CONFORME O TEMPO DO DIA

tempo = input("Digite como o tempo esta (Ensolarado, Chuvoso, Nublado, Frio, Calor): ").strip() .lower()

match tempo:
    case "ensolarado":
        print("Use oculos de sol.")
    case "chuvoso":
        print("Leva guarda-chuva.")
    case "nublado":
        print("Talvez chova! Leva guarda-chuva.")
    case "frio":
        print("Leva blusa de frio.")
    case "calor":
        print("Usa roupa leve.")
    case _:
        print("Dado invalido!!!")
