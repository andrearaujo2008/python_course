import datetime

# Vai armazenar a data e hora do sistema
agora = datetime.datetime.now()
# Formatar data do sistema atual
hora_formatada = agora.strftime("%H:%I")

# Mostrar a data atual
print(f"A data de hoje é: {hora_formatada}")
