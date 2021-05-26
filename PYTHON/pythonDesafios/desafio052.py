num = int(input('Digite um numero inteiro:'))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('[34m', end='')
        tot += 1
    else:
        print('[34m', end='')
    print(f'{c}',end='')
print(f'n033[m O numero {num} foi divisivel por {tot} vezes. ')
if tot == 2:
    print('E por isso ele e PRIMO.')
else:
    print('E por isso ele NAO e PRIMO!.')
