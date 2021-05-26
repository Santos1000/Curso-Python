gols = list()    # INPUT DE DADOS, FORMATAÇAO E SELECAO DE OBJETO DE LISTA
galera = list()
dados = dict()
while True:
    dados.clear()
    dados['nome'] = str(input('Nome do jogador(a): '))
    dados['partidas'] = int(input(f'Quantas partidas {dados["nome"]} fez: '))
    gols.clear()
    for n in range(1, dados['partidas'] + 1):
        gols.append(int(input(f'Quantos gols na partida {n}: ')))
    dados['Gols'] = gols[:]
    dados['total'] = sum( gols )
    galera.append(dados.copy())
    while True:
        resp = str(input('Quer continuar: [s;n]')).strip().upper()
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp in 'N':
        break
print('==='*20)
print('Cod: ', end='')
for i in dados.keys():
    print(f'{i:<15}', end='')
print()
print('==='*20)
for k, v in enumerate(galera):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print()
print('==='*20)
while True:
    busca = int(input('Mostrar dados de qual jogaror(a):(999 para parar)'))
    if busca == 999:
        break
    if busca >= len(galera):
        print(f'Erro ! Não existe jogador(a) com código {busca}.')
    else:
        print(f' --- LEVANTAMENTO DO JOGADOR {galera[busca]["nome"]}:')
        for i, g in enumerate(galera[busca]['Gols']):
            print(f'     No jogo {i} fez {g} gols')
    print('--'*40)
print('<< VOLTE SEMPRE >>')
