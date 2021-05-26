from datetime import date
nasc = int(input('Qual a idade do atleta:'))
idade = (nasc - date.today().year)*-1
if idade <= 9:
    print(f'O atleta possui {idade} anos, e sua categoria e: MIRIM.')
elif idade <= 14:
    print(f'O atleta possui {idade} anos, e sua categoria e: INFANTIL.')
elif idade <= 19:
    print(f'O atleta possui {idade} anos, e sua categoria e: JUNIOR.')
elif idade <= 25:
    print(f'O atleta possui {idade} anos, e sua categoria e: SENIOR.')
elif 25 < idade:
    print(f'O atleta possui {idade} anos, e sua categoria e: MASTER.')
