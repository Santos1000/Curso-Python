lista = []
while True:
    n = lista.append(int(input('Digite um valor:')))
    resp = str(input('Você quer continuar: [s;n]')).strip().upper()[0]
    if resp in 'Nn':
        break
print('-=---'*10)
print(f'Você digitou {len(lista)} elementos:')
lista.sort(reverse=True)
print(f'Os valores em ordem decrecente são: {lista}')
if 5 in lista:
    print( f'O número 5 aparece na lista' )
else:
    print( 'O valor 5 não foi encontrado na lista.' )

