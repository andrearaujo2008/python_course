# Exemplo de uma função com retorno de múltiplos valores, agora usando indice para mostrar todos os valores ou
# um especifico valor

def calcular_operacoes(a, b):  # Aqui estou declarando a funcao

    soma = a + b
    subtracao = a - b
    multiplicacao = a * b
    divisao = a / b
    return soma, subtracao, multiplicacao, divisao  # Atribuindo os calculos feitos


resultado = calcular_operacoes(8, 2)  # Aqui ele vai guardar todos os resultados da operacao

print(resultado)  # Saida será soma = 10 subtracao = 6 multiplicacao = 16 divisao = 4


# Sempre o indice começa no 0
print(resultado[2])  # Aqui no caso eu quero mostra um resultado da indice, no qual seria multiplicacao que será 16
