print('---'*10)
print('SEQUENCIA DE FIBONACCI')
print('---'*10)
n = int(input('Digite quantos termos voce quer mostrar:'))
t1 = 0
t2 = 1
cont = 3
print('~'*40)
print(f'{t1} -> {t2}', end='')
while cont <= n:
    t3 = t1 + t2
    print(f'-> {t3}', end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' -> FIM')
print('~'*40)