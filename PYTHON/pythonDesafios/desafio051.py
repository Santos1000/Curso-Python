print(f'{" OS 10 TERMOS DE UMA PA ":=^40}')
num = int(input('Digite quantos termos:'))
r = int(input('digite sua razao:'))
decimo = num + (10 - 1) * r
for c in range(num, decimo, r):
    print(f'{c}', end=' -> ')
print('ACABOU')

