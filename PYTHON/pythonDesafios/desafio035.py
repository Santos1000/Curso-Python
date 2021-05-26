print('-.-'*15)
c1 = float(input('Qual a primeira medida? '))
c2 = float(input('Qual a segunda medida? '))
c3 = float(input('Qual a terceira medida? '))
print('-.-'*15)
if c1 < c3 + c2 and c2 < c1 + c3 and c3 < c2 + c1:
    print(' E possive formar um triangulo!')
else:
    print('Nao e possivel formar um triangulo')
