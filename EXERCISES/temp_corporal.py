# Mede temperatura corporal para ver se esta com febre ou nao

temp = float(input('Digite a temperatura corporal: '))

if temp >= 36 and temp <= 37:
    print('Sua temperatura corporal esta OK')
else:
    print('Procure o medico imediatamente')
