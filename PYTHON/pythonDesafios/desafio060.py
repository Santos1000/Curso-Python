'''from math import factorial
num = int(input('Digite um número para saber seu fatorial:'))
f = factorial(num)
print(f'O fatorial de {num} é {f}')'''

num = int(input('Digite um número para saber seu fatorial:'))
c = num
f = 1
print(f'Calculando fatorial de {num}!= ', end='')
while c > 0:
    print(f'{c}', end= '')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f'{f}')
#print(f'O fatorial de {num} é {f}')
