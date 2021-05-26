total = mil = menor = cont = 0
barato = ''
while True:
    print('--'*20)
    print('LOJAS SUPER BARATÃO')
    print('--'*20)
    produto = str(input('Nome do produto: ')).strip().upper()
    preço = float(input('Preço: '))
    cont += 1
    total += preço
    if preço >= 1000:
        mil += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    resp = ' '
    while resp not in 'NS':
        resp = str( input( 'Quer continuar:[s;n] ' ) ).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O total da compra foi de R$ {total:.2f}')
print(f'Temos {mil} produto(s) custando mais de R$1.000,00. ')
print(f'O produto mais marato foi a;o {barato} que custa R$ {menor:.2f}.')
