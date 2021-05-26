lista = []
while True:
    n = (int(input('Digite um valor:')))
    if n not in lista:
        lista.append(n)
        print('Valor adicionado com suesso')
    else:
        print('Valor já existente na lista')
    resp = str(input('Quer continuar:[s;n] ')).strip().upper()[0]
    if resp in 'Nn':
        break
print('--'*20)
lista.sort()
print(f'Você digitou os números: {lista}')
print('PROGRAMA ENCERRADO')