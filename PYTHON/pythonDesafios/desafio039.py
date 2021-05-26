'''from datetime import date
nasc = int(input('Em que ano voce nasceu?'))
alistamento = nasc + 18
idade = nasc - date.today()
data = alistamento - date.today()
if alistamento == date.today():
    print(f'Quem nasceu em {nasc} tem {idade} anos .Voce tem que se alistar urgentemente!!')
elif alistamento > date.today().year:
        tempo1 = alistamento - date.today().year
    print(f'Quem nasceu em {nasc} tem {idade} anos.Voce esta atrasado {tempo1} anos.')
elif alistamento < date.today().year:
tempo2 = nasc - alistamento
print(f'Quem nasceu em {nasc} tem {idade} anos. Voce ainda e muito novo, faltam {tempo2} anos para o seu alistamento.')'''

from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento:'))
idade = atual - nasc
print(f'Quem nasceu em {nasc} e tem {idade} anos .')
if idade == 18:
    print('Voce tem que se alistar urgentemente!!')
elif idade < 18:
    saldo = (idade - 18)* -1
    ano = nasc + saldo
    print(f'Voce ainda e muito jovem, falta ainda {saldo} anos para seu alistamento, prepare-se para o ano de {ano}!')
elif idade > 18:
    saldo = idade - 18
    ano = nasc - saldo
    print(f'Voce ja passou da idade de se alistar {saldo} anos, correspondente a {ano}.')
