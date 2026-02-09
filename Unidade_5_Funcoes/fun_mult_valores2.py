# Exemplo de uma função com retorno de múltiplos valores, porem usando alguns valores serao retornado
# nao precisando usar todos eles

def calcular_operacoes(a, b):  # Aqui estou declarando a funcao

    soma = a + b
    subtracao = a - b
    multiplicacao = a * b
    divisao = a / b
    return soma, subtracao, multiplicacao, divisao  # Atribuindo os calculos feitos


s1, s2, _, _ = calcular_operacoes(8, 2)  # Aqui s1 está somando 5+2 e a multiplicacao e divisao não estou usando

print(s1, s2)  # Saida no qual o resultado será s1 10 e s2 será 6
