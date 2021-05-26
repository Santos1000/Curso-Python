sal = float(input('Qual o valor do salario do funcionario?'))
if sal >= 1250:
    s1 = sal*0.1
    print(f'O aumento sera de 10%, ficando com um total de: R${sal + s1:.2f}.')
else:
    s2 = sal*0.15
    print(f'O aumento sera de 15%, ficando com um total de: R${sal + s2:.2f}.')

