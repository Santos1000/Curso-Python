cont = total = soma = 0
cont = int(input('Digite um número [999 para parar]:'))
while cont != 999:
   total += 1
   soma += cont
   cont = int(input('Digite um número [999 para parar]:'))
print(f'Voce digitou {total} números e a soma entre eles foi {soma}.')
