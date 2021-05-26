from random import randint  # NÃO FUNCIONANDO ESSE JOGO
from time import sleep
lista = list()
jogos = list()
print('--='*20)
print('Jogo da MEGA SENA')
print('--='*20)
quant = int(input('Digite a quantidade de jogos que deseja: '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot =+ 1
print(f'Os números sorteados foram {jogos}')
print('=='*10,f'Sorteando {quant} jogos','=='*10)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1} : {l}')
    sleep(1)
print('--'*5,'Boa SORTE','--'*5)