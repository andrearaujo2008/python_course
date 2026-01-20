
# Exercicio 4.13
frase = input("Digite uma frase: ").strip()
# Separa a frase em formato lista e remove todos os espaços em branco desnecessários.
lista = frase.split()

# Junta as palavras que estava em listas.
nova_frase = " ".join(lista)

# Resultado final
print(f"A nova frase é: {nova_frase}")
