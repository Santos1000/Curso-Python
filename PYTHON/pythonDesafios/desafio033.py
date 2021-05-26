a = int(input('Digite numero:'))
b = int(input('Digite numero:'))
c = int(input('Digite numero:'))
#verificando o menor e maior
menor = a
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
print(f'O maior numero e {maior}, e o menor {menor}.')

