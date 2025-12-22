# Contar vogais a, e, i, o, u
# Desenvolvido por: Andre de Araujo
# Data 04/12/2025

palavra = input("Digite um palavra: ").strip().lower()

contador = 0
vg_enc = ""

for letra in palavra:
    if letra in "aeiou":
        contador += 1
        vg_enc += letra
print(f"O nome {palavra} tem {contador} vogais")
print(f"Vogais encontradas: {vg_enc} ")
