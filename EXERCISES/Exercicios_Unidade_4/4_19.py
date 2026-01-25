
import datetime

# Forma correta de criar um objeto datetime para data e hora exatas:
data = datetime.datetime(2022, 1, 15, 12, 0)

# Para exibir no formato: "15/01/2022 12:00"
form_data = data.strftime("%d/%m/%Y %H:%M")
print(form_data)
