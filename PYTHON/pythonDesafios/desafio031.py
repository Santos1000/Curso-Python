dist = float(input('Qual e a distancia do percurso:'))
if dist >= 200:
    p1 = dist * 0.50
    print(f'Sera cobrado o valor de R$0.50/KM , sendo assim, o valor da sua corrida sera de: R${p1:.2f}.')
else:
    p2 = dist * 0.45
    print(f'Sera cobrado o valor de R$0.45/KM , sendo assim, o valor da sua corrida sera de: R${p2:.2f}.')
print('Tenha uma boa viagem!')
