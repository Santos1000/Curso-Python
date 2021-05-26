resp = 'S'
quant = media = soma = 0
while resp in 'S':
    num = int(input('Digite um número:'))
    quant += 1
    soma += num
    if quant == 1:
        maior = menor = num
    elif num > maior:
        maior = num
    elif num < menor:
        menor = num
    resp = str(input('Quer continuar S ou N:')).upper().strip()[0]
media += soma / quant
print(f'Voce digitou {quant} números e a media foi {media:.2f}.')
print(f'O maior valor digitado foi {maior} e o menor foi {menor}.')
