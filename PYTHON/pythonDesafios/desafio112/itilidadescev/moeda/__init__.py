def aumentar(preço=0, taxa=0, formato=False):
    res = preço + (preço * taxa / 100)
    return res if not formato else moeda( res )


def diminuir(preço=0, taxa=0, formato=False):
    res = preço - (preço * taxa / 100)
    return res if not formato else moeda( res )


def dobro(preço=0, formato=False):
    res = preço * 2
    return res if not formato else moeda( res )


def metade(preço=0, formato=False):
    res = preço / 2
    return res if not formato else moeda( res )


def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:.2f}'.replace( '.', ',' )


def resumo(preço=0, taxaa=0, taxar=0):
    print( '-' * 30 )
    print( 'RESUMO DO VALOR'.center( 30 ) )
    print( '-' * 30 )
    print( f'O preço analisado\t    {moeda( preço )} ' )
    print( f'O dobro do preço é:\t    {dobro( preço, True )}' )
    print( f'A metade do preço é:\t{metade( preço, True )}' )
    print( f'{taxaa}% de aumento:\t\t\t{aumentar( preço, taxaa, True )}' )
    print( f'{taxar}% de reduçao:\t\t\t{diminuir( preço, taxar, True )}' )
    print( '-' * 30 )