
import re

texto = input("Escreva uma frase:").strip().lower()
# artigos em português (definidos e indefinidos)
padrao = r"\b(o|a|os|as|um|uma|uns|umas)\b"
# remove artigos, ignorando maiúsculas/minúsculas
sem_artigos = re.sub(padrao, "", texto, flags=re.IGNORECASE)

# remove espaços duplicados que podem sobrar
sem_artigos = re.sub(r"\s+", " ", sem_artigos).strip()

print("Frase sem artigos:", sem_artigos)
