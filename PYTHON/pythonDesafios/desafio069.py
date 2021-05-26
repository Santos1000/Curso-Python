maior18 = menor20f = homens = 0
while True:
    print('--'*20)
    print('CADASTRE UMA PESSOA')
    print('--'*20)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo:[M;F] ')).upper().strip()[0]
    if idade >= 18:
        maior18 += 1
    if sexo == 'F'and idade < 20:
        menor20f += 1
    if sexo == 'M':
        homens += 1
    contin = ' '
    while contin not in 'SN':
        contin = str(input('Quer continuar:[S;N] ')).upper().strip()[0]
    if contin == 'N':
        break
print('Acabou')
print(f'São {maior18} pessoas maiores de 18 anos.')
print(f'São {menor20f} mulheres menor de 20 anos.')
print(f'São {honens} ao todo.')
