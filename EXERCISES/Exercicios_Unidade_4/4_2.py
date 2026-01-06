import math
import locale

locale.setlocale(locale.LC_ALL, 'pt_PT.UTF-8')

n = float(input("Insira um numero: "))
raiz = math.sqrt(n)

v_monetario = locale.currency(raiz, grouping=True)

print(f"A raiz quadrada do numero informado e: {v_monetario}")
