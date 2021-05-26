while True:
    n = int(input('Quer ver a tabuada de qual valor: '))
    print( '--' * 20 )
    if n < 0:
        break
    print('--' * 20)
    for c in range(1, 11):
        print(f'{n} X {c} = {c*n}')
print('PROGRAMA DE TABUADA ENCERRADO.VOLTE SEMPRE!')
