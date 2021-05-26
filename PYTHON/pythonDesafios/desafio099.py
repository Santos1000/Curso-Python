from time import sleep


def maior(* núm):
    cont = maior = 0
    print()
    print( f'Analisando os valore...')
    for valor in núm:
        print(f'{valor}', end='  ', flush=True)
        sleep( 0.3 )
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} ao todo')
    print(f'O maior valor foi {maior}')


# PROGRAMA PRINCIPAL
maior( 2, 9, 4, 5, 7, 1 )
maior( 4, 7, 0 )
maior( 1, 2 )
maior( 6 )
maior()
