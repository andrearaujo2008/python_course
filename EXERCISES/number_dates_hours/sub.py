import re

texto = "Python 3 e incrivel!"
novo_texto = re.sub(r"\d", "4", texto)
print(novo_texto)  # Saida: Python 4 é incrivel!.
