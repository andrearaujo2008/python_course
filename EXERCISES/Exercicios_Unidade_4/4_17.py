import datetime

# Vai armazenar a data e hora do sistema
agora = datetime.datetime.now()
# Formatar data do sistema atual
data_formatada = agora.strftime("%d/%m/%Y")

# Mostrar a data atual
print(f"A data de hoje é: {data_formatada}")
