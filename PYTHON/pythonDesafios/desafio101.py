def voto(ano):
    from datetime import date
    hoje = date.today().year
    idade = hoje - ano
    print(f'Com {idade} anos:')
    if idade < 18 or idade >=95:
        print('VOTO OPCIONAL')
    elif idade < 16:
        print('NÃO VOTA')
    else:
        print('VOTO OBRIGATÓRIO')


ano = int(input('Em que ano você nasceu: '))
print(voto(ano))

