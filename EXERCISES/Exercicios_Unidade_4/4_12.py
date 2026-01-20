

frase = input("Insere uma frase: ")

palavras = frase.split()

conta_o = sum([1 for palavra in palavras if palavra.endswith("o")])
conta_a = sum([1 for palavra in palavras if palavra.endswith("a")])

print(f"Palavras que tem o na frase: {conta_o}")
print(f"Palavras que tem o na frase: {conta_a}")
