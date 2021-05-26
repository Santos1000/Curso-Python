tudo = []
dados = []
maior = menor = 0
while True:
    dados.append(str(input('Digite um nome: ')))
    dados.append(float(input('Digite seu peso: ')))
    if len(tudo) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    tudo.append(dados[:])
    dados.clear()
    resp = (str(input('Quer continuar:(s;n) ')))
    if resp in 'nN':
        break
print('--'*30)
print(tudo)
print(f'Foram cadastradas {len(tudo)} pessoas')
for c in tudo:
    if c[1] == maior:
        print(f'O {c[0]} foi a pessoa mais gorda.')
for c in tudo:
    if c[1] == menor:
        print(f'O {c[0]} foi a pessoa mais magra.')
print(f'Maior peso {maior} e o menor peso {menor}')
