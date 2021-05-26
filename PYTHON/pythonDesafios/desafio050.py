cont = 0
soma = 0
for c in range(1, 7):
    num = int(input('Digite um valor:'))
    if num % 2 == 0:
         soma += num
         cont += 1
print(f'A soma dos {cont} numero(s) par(es) e = {soma}')