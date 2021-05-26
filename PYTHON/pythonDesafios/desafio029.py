V = float(input('Qual a velocidade atual:'))
if V > 80:
    M = (V - 80)*10
    print(f'Voce excedeu a velocidade e foi multado em R${M:.2f}')
else:
    print('Mantenha a velocidade, excelente!')
print('Mantenha a atencao no transito.')
