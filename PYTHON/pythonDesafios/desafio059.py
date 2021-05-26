from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opçao = 0
while opçao != 5:
    print( '[ 1 ] somar\n[ 2 ] multiplicar\n[ 3 ] maior\n[ 4 ] novos numeros\n[ 5 ] saia do programa')
    opçao = int( input( '>>>>> Qual é a sua opçao: ' ))
    if opçao == 1:
        z = n1 + n2
        print(f'A soma de {n1} + {n2} = {z} .')
    elif opçao == 2:
        m = n1 * n2
        print(f'A multiplicaçao de {n1} X {n2} = {m}.')
    elif opçao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
            print( f'Entre {n1} e {n2} o maior número é {maior}.' )
    elif opçao == 4:
        print('Informe os números novamente:')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opçao == 5:
        print( 'Finalizando...')
    else:
        print('Tente novamente, opçao inválida.')
    print('-='*10)
    sleep(2)
print('Fim do programa, volte sempre!')

