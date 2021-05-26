print('Gerador de PA\n','==-'*10)
primeiro = int(input('Primeiro termo:'))
razao = int(input('Razao da PA:'))
termo = primeiro
c = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while c <= total:
        print(f'{termo} ->', end='')
        c += 1
        termo += razao
    print('PAUSA')
    mais = int(input('Quantos termos voce quer mostrar a mais:'))
print(f'FIM , a progressão mostrou {total} termos.')
