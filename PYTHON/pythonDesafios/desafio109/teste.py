from desafio109 import moeda

p = float(input('Digite o preço: R$ '))
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, True)}.')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}.')
print(f'Diminuindo 10% , temos {moeda.diminuir(p, 10, True)}')
print(f'Aumentando 20% , temos {moeda.aumentar(p, 20, True)}')