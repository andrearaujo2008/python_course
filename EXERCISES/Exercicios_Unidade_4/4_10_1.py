
import re

frase = input("Insira uma frase: ")
padrao = r"\b(eu|tu|ele|ela|nós|vós|eles|elas)\b"
palavra = re.sub(padrao, " ", frase, flags=re.IGNORECASE)

palavra = re.sub(r"\s+", " ", palavra).strip()

print(f"A frase sem pronomes pessoais e: {palavra}")
