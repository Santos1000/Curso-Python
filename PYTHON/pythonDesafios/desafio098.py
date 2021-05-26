from time import sleep          #ROTINA DEF
def contador(i, f , p):
    print( '--' * 20 )
    print(f'Contagem de {i} até {f} de {p} em {p}:')
    if p < 0:
        p *= -1
    if p ==0:
        p = 1
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}', end=' ', flush=True)
            cont += p
            sleep( .5 )
        print()
    else:
        cont = i
        while cont >= f:
            print(f'{cont}', end=' ', flush=True)
            cont -= p
            sleep( .5 )
        print()


contador(1, 10, 1)          #PROGRAMA PRINCIPAL
contador(10, 0, 2)
print('--'*20)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Início: '))
fi = int(input('Final: '))
pa = int(input('Paço: '))
contador(ini, fi, pa)
print('FIM!!')