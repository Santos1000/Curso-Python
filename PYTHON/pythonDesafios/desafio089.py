'''lista = [[[],[],[]],[]]
while True:
    lista[0][0].append(str(input('Nome: ')))
    n1 = lista[0][1].append(float(input('Prova 2: ')))
    n2 = lista[0][2].append(float(input('Prova 1: ')))
    media = lista[1].append((n1 + n2) /  2)
    resp = (str( input( 'Quer continuar: s;n ')))
    if resp in 'Nn':
        break
print(f'Nomes {lista}')
print('--'*20)
print(f'Notas do semestre')
print(f'{"Numero":4}{"Aluno":<8}{"Nota":>14}')
for c,n in enumerate(lista[0]):
    print(f'{c}{n(lista[0])}{n(lista[1])}')
print(lista[0])
print('--'*20)
print(lista[1])
print()
print(lista[0][1])
'''