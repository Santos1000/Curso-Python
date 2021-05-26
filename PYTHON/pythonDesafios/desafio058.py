from random import randint
from time import sleep
palpite = 0
print('Sou seu computador ...')
sleep(1)
print('Acabei de pensar em um número entre 0 e 10.')
sleep(1)
print('Será que você consegue adivinhar qual foi!')
x = randint(0,10)
acertou = False
while not acertou:
    num = int( input( 'Qual é seu palpite: ' ))
    palpite += 1
    if num == x:
        print( f'Acertou com {palpite} tentativas.' )
        acertou = True
    elif num > x:
        print('Menos... Tente mais uma vez.')
    elif num < x:
        print('Mais... Tente mais uma vez.')
