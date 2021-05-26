listagem = ('BORRACHA', 1, 'LÁPIS', 0.7, 'CADERNO', 16.0,
            'ESTOJO', 5,'TRANSFERIDOR', 2, 'COMPASSO', 10,
            'MOCHILA', 120,'CANETAS', 22.30,'COLA', 4)
print('--'*20)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('--'*20)
for pos in range(0, len(listagem)):
    if pos % 2 == 0 :
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>8.2f}')
