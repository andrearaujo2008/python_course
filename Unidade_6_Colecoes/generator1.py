def gerar_pares():
    atual = 0
    while atual >= 0:
        yield atual
        atual += 2


pares = gerar_pares()
par = next(pares)

while par <= 10:
    print(par, end=" , ")
    par = next(pares)