def escr(msg):
    tam = len(msg)
    print('~'*tam)
    print(msg)
    print('~'*tam)

for c in range(0,4):
    msg = str(input('Escreva uma palavra: '))
    escr(msg)