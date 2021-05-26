from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1, 8):
    nasc = int(input(f'Em que ano a {pess} nasceu:'))
    idade = atual - nasc
    if idade <= 18:
        totmenor += 1
    else:
        totmaior += 1
print(f'Ha {totmenor} pessoas e menores de idade, e {totmaior} pessoas maiores de idade.')
