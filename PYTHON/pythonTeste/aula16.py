'''num = [2,5,6,9]
num[2] = 3
num.append(70)
num.sort(reverse=True)
num.insert(2, 2)
num.pop(1)
if 5 in num:
    num.remove(5)
else:
    print('não há número 4 ')
print(num)
print(f'Essa lista tem {len(num)} elementos')'''

'''valores = []
valores.append(5)
valores.append(10)
valores.append(4)
for c,v in enumerate(valores):
    print(f'Naposição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista')'''

'''valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor:')))
for c, v in enumerate( valores ):
    print( f'Naposição {c} encontrei o valor {v}!' )
print( 'Cheguei ao final da lista' )'''

a = [2, 3, 4, 7]
b = a[:] #copia para edição
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
