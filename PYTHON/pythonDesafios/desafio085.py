''' COM DUAS LISTAS
pares = []
impar = []
for c in range(1,8):
    num = (float(input(f'Digite o {c} valor: ')))
    if num % 2 == 0:
        pares.append(num)
    else:
        impar.append(num)
        print('--'*30)
print(f'Os valores pares digitados foram: {pares}')
print(f'Os valores impares digitados foram: {impar}')'''

lista = [[],[]]
num = 0
for c in range(1,8):
    num = (int(input(f'Digite o {c} valor: ')))
    if num % 2 ==0:
        lista[0].append(num)
    else:
        lista[1].append(num)
lista[0].sort()
lista[1].sort()
print('--'*30)
print(f'Os valores pares digitados foram: {lista[0]}')
print(f'Os valores impares digitados foram: {lista[1]}')