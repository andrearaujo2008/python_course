

date_str = input("Enter a date (DD/MM/YYYY): ")

if len(date_str) == 10 and date_str[2] == '/' and date_str[5] == '/':
    dia = int(date_str[:2])
    mes = int(date_str[3:5])
    ano = int(date_str[6:])

    if (1 <= dia <= 31) and (1 <= mes <= 12) and (1 <= ano <= 9999):
        print("Data valida no formato dd/mm/aaaa.")
    else:
        print("Data invalida no formato dd/mm/aaaa")
else:
    print("O texto nao corresponde a uma data")
