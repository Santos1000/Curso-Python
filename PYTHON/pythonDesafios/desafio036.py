print('--==--'*10)
print('Aprovacao de credito imobiliario')
print('--==--'*10)
casa = float(input('Qual o valor do imovel?'))
sal = float(input('Qual o valor da sua renda?'))
div = int(input('Em quantos anos pretende financiar?'))
minimo = sal*0.3
custo = casa / (div*12)
if custo <= minimo:
    print(f'A casa podera ser financiada por um valor de R${custo:.2f} ao mes dentro de {div}anos.')
else:
    print(f'O credito nao podera ser liberado.')
