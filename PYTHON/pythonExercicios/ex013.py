sal = float(input('Digite o valor do salario:'))
n = float(input('Qual o valor da promocao em porcentagem?'))
promo = sal + (sal * n / 100)
print(f"O funcionario vai ganhar com {n}% de aumento R${promo}")
