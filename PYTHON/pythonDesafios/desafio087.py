lista = [[0, 0 , 0], [0, 0, 0], [0, 0, 0]]# MATRIZ
spar = maior = scoluna = 0
for l in range(0,3):
    for c in range(0,3):
        lista[l][c] = int(input(f'Digite um valor para {[l], [c]} :'))
for l in range(0, 3):                     # ViZUALIZAÇAO DA MATRIZ
    for c in range(0, 3):
        print(f'[{lista[l][c]:^4}]', end='')
        if lista[l][c] % 2 == 0:          # VALORES PARES
            spar += lista[l][c]
    print()
print( '--' * 30 )
print( f"A soma dos valores pares é: {spar}" )
for l in range(0, 3):                     # SELECAO DE COLUNA
    scoluna += lista[l][2]
print(f'A soma dos valores da 3 coluna é: {scoluna}')
for c in range(0, 3):                     # SELECAO DE LINHA + MAIOR
    if c == 0 or lista[1][c] > maior:
        maior = lista[1][c]
print(f'O maior elemento da linha 2 é: {maior}')