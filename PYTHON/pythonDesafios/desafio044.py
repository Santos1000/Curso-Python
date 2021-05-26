print( f'{"LOJAS GUANABARA":=^40}' )
reais = float(input('Preco das compras: R$'))
print('FORMA DE PAGAMENTO')
print('[ 1 ] a vista dinheiro/cheque \n[ 2 ] a vista cartao')
print('[ 3 ] 2x no cartao \n[ 4 ] 3x ou mais no cartao')
num = int(input('Qual e a opcao?'))
if num == 1 :
    print(f'A vista, com 10% de desconto. Valor a pagar = R${reais - (reais*0.1)}')
elif num == 2 :
    print(f'A vista no cartao, com desconto de 5%. Valor a pagar = R${reais - (reais*0.05)}')
elif num == 3 :
    print(f'2x no cartao. Valor a pagar por parcela = R${reais / 2}')
elif num == 4 :
    totparc = int(input('Quantas parcelas?'))
    print(f'{totparc}x no cartao. Valor a pagar por parcela acrescido de 20% juros = R${(reais + (reais * 0.2)) / totparc}')

