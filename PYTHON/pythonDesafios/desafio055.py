menor = 0
maior = 0
for c in range(1, 6):
    peso = float(input(f'Qual o peso da {c} pessoa: '))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso >= maior:
            maior = peso
        if peso <= menor:
            menor = peso
print(f'O maior peso e {maior} e o menor peso {menor}.')
