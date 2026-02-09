# Exemplo de uma função com retorno de múltiplos valores

def calcular_operacoes(a, b):  # Aqui estou declarando a funcao

    soma = a + b
    subtracao = a - b
    return soma, subtracao  # Atribuindo os calculos feitos


s1, s2 = calcular_operacoes(5, 2)  # Aqui s1 está somando 5+2 e o s2 esta subtraindo 5 - 2

print(s1, s2)  # Saida no qual o resultado será s1 7 e s2 será 3
