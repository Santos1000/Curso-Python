from random import randint
from time import sleep
itens = ('PEDRA','PAPEL','TESOURA')
print('*---*'*10)
print('Vamos jogar JO KEN PO')
print('*---*'*10)
print('Suas opcoes:\n [ 0 ] PEDRA \n [ 1 ] PAPEL \n [ 2 ] TESOURA')
num: int = int(input('Qual e a sua jogada? '))
print(' JO ' )
sleep(1)
print(' KEN ' )
sleep(1)
print(' PO ' )
sleep(1)
print('=='*10)
n = randint(0, 2)
if n == num:
    print('Empateee!!')
elif num == 0 and n == 1:
    print(f'PERDEU!!O Computado escolheu papel, sua pedra e envolvida.')
elif num == 0 and n == 2:
    print(f'VENCEU!! O Computado escolheu TESOURA.')
elif num == 1 and n == 0:
    print(f'VENCEU!! O Computador escolheu PEDRA.')
elif num == 1 and n == 2:
    print(f'PERDEU!! O Computador escolheu TESOURA.')
elif num == 2 and n == 1:
    print(f'VENCEU!! O Computados escolheu {itens[n]}')
elif num == 2 and n == 0:
    print('PERDEU!!')
else:
    print('ERRO.Tente novemente com as opcoes acima.')

