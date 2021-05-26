print(f'{" OS 10 TERMOS DE UMA PA ":=^40}')
primeiro = int(input('Digite o primeiro termo:'))
razao = int(input('digite sua razao:'))
c = 1
termo = primeiro
while c <= 10:
    print(f'{termo} -> ', end= '')
    termo += razao
    c += 1
print('ACABOU')