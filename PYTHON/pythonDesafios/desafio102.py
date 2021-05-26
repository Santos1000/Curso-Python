def fatorial(n= 1, show = False):
    """
        --> calculo de fatorial
    :param num: numero a ser calculado
    :param show: opção de mostrar ou não o calculo completo
    :return: fatorial se repetindo
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c , end='')
            if c > 1:
                print(' x ',end='')
            else:
                print(' = ',end='')
        f *= c
    return f


n = int(input('Digite um número:'))
print(f'O fatorial de {n} é igual a {fatorial(n, show= True)}')
help(fatorial)