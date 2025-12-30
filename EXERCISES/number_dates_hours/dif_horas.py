# Subtrai horas que falta entre os numeros.
import datetime
instante1 = datetime.datetime(2023, 6, 9, 8, 0)  # Data 2023
instante2 = datetime.datetime(2024, 6, 9, 8, 0)  # Data 2024
diferenca = instante2 - instante1

dif_horas = diferenca.total_seconds() / 3600
print("Diferenca em horas", dif_horas)
