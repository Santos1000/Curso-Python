'''LIGAÇAO ENTRE LISTAS
teste = list()
teste.append('Bárbara')
teste.append(24)
print(f'{teste}')
galera = list()
galera.append(teste[:])
teste[0] = 'Debora'
teste[1] = 33
galera.append(teste)
print(f'{galera}')'''


'''LISTAGEM COMPOSTA
galera = [['João', 19], ['Ana', 33], ['Joaquina', 13], ['Maria', 45]]
#  print(galera[2][1])
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade.')'''


galera = []
dado = []
totmaior = totmenor = 0
for c in range (0, 3):
    dado.append(str(input('Nome:')))
    dado.append(int(input('Idade:')))
    galera.append(dado[:])
    dado.clear() # retirou galera
print(galera)
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmaior =+ 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmenor =+ 1
print(f' Temos {totmaior} maiore(s) e {totmenor} menore(s) de idade.')

