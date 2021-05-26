lista = []
par = []
impar = []
while True:
    num = lista.append(int(input('Digite um número: ')))
    resp = (str(input('Quer continuar: [s;n] ')))
    if resp in 'Nn':
        break
listapar = lista[:]
for c,v in enumerate(listapar):
    if v % 2 ==0:
        par.append(v)
    else:
        impar.append(v)
print('--'*30)
print(f'A lista completa é {lista}')
print(f'A lista de valores pares é  {par}')
print(f'A lista de valores impares é {impar}')
