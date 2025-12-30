import datetime

data_original = datetime.datetime(2025, 6, 9)
dez_dias = datetime.timedelta(days=10)
data_nova = data_original - dez_dias

print("Data original: ", data_original)
print("Data nova", data_nova)
