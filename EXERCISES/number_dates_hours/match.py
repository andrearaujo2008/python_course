# Aqui ele vai verificar se a palavra Python se encontra no inicio ou nao.
import re  # Precisa dessa biblioteca para trabalhar com match

texto = " e poderoso Python."
if re.match("Python", texto):
    print("Comeca com Python.")
else:
    print("Nao comeca com Python")
