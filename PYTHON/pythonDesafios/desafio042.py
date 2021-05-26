print('--- . ---'*10)
print('Vamos formar triangulos e ver a qual tipo pertencem!')
print('--- . ---'*10)
l1 = float(input('A primeira medida:'))
l2 = float(input('A segunda medida:'))
l3 = float(input('A terceira medida:'))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('E possivel formar triangulo!')
    if l1 == l2 == l3:
        print('Temos um triangulo: EQUILATERO.')
    elif l1 != l2 != l3 !=l1:
        print('Temos um triangulo: ESCALENO.')
    else:
        print('Temos um triangulo: ISOSCELES.')
else:
    print('NAO podemos formar triangulo, tente outro valor.')
