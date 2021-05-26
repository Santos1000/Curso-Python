from random import randint
print('-=-'*10)
num = int(input('Adivinhe um numero de 0 a 5 :'))
print('-=-'*10)
N = randint(0,5)
print('O numero escolhido foi: {}.'.format(N))
if N == num:
    print('O Numero escolhico esta certo!Voce leu minha mente.')
else:
    print('O Numero escolhido esta errado, tente novamente!')

