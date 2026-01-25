
# biblioteca usando data
import datetime

# Pega a hora e data atual do sistema.
data = datetime.datetime.now()
# Formato da data dd-mm-yyyy
agora = data.strftime("%d-%m-%Y")

# Mostra o resultado.
print(f" A data de hoje é: {agora}")
