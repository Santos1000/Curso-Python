'''nome = str(input('Qual e seu nome?'))
if nome == 'Gustavo':
    print('Que nome lindo voce tem')
else:
    print('Seu nome e tao exotico!')
print('Bom dia , {} !'.format(nome))'''

n1 = float(input('Nota Prova 1:'))
n2 = float(input('Nota Prova 2:'))
m = (n1 + n2)/2
print(f'Sua media e {m}.')
if m < 7:
    print('Reprovado.')
else:
    print('Aprovado.')
print('--FIM--')
