
import re  # biblioteca para usar o regex

frase = input("Insere a frase: ")

padrao = r"\b(de|do|da|dos|das|em|no|na|nos|nas|por|para|com|sem)\b"  # inserido as preposiçoes

preposicao = re.sub(padrao, "", frase, flags=re.IGNORECASE)

preposicao = re.sub(r"\s+", " ", preposicao).strip()

print(f"A frase sem preposicao é: {preposicao}")
