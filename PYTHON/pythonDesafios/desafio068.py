from random import randint
v = 0
print('=-'*20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-'*20)
while True:
    jogador = int(input('Diga um valor:'))
    comp = randint(0, 10)
    total = jogador + comp
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar: [P ou I] ')).strip()[0].upper()
    print(f'Voce jogou {jogador} e o computador {comp}. total deu {total}')
    print('Deu PAR!' if total % 2 == 0 else 'Deu IMPAR!')
    if tipo =='P':
        if total % 2 == 0:
            print('Voce venceu')
            v += 1
        else:
            print('voce perdeu')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('voce venceu!')
            v += 1
        else:
            print('Voce perdeu!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER. VOCE VENCEU {v} VEZES.')
