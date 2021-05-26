totmulher20 = 0
somaidade = 0
mediaidade = 0
maioridadedehomem = 0
nomevelho = ' '
for p in range( 1, 5 ):
    print(f'----- {p}PESSOA -----')
    nome = str(input( 'NOME: ')).strip().capitalize()
    idade = int(input( 'IDADE: '))
    sexo = str(input( 'SEXO [M ou F]: ')).strip().upper()
    somaidade += idade
    mediaidade = somaidade / 4
    if p == 1 and sexo in 'Mm':
        maioridadedehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadedehomem:
        maioridadedehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade > 20:
        totmulher20 += 1
print(f'A media do grupo e {mediaidade} anos.')
print(f'O homem mais velho tem {maioridadedehomem} anos e se chama {nomevelho}.')
print(f'Ao todo sao {totmulher20} mulheres com menos de 20 anos.')
