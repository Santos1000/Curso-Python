p1 = float(input('Nota prova 1:'))
p2 = float(input('Nota prova 2:'))
m = (p1 + p2)/2
print(f'A media entre a P1 e a P2 e = {m:.1f}.')
if m < 5.0:
    print('REPROVADO')
elif 5 <= m < 6.9:
    print('RECUPERACAO')
elif m >= 7.0:
    print('APROVADO!')
