gols = list()
dados = dict()
dados['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantos partidas {dados["nome"]} jogou: '))
for j in range(1, partidas + 1):
    gols.append(int(input(f'Quantos gols na partida {j} : ')))
dados['Gols'] = gols
dados['total'] = sum(gols)
print('-='*30)
print(dados)
print('-='*30)
for c,l in dados.items():
    print(f'O campo {c}, tem o valor de {l}')
print('-='*30)
print(f'O jogador(a) {dados["nome"]} fez participou de {len(dados["Gols"])} jogos')
for i, v in enumerate(dados['Gols']):
    print(f' -> Na partida {i}, fez {v} gols')
print(f'Foi um total de {dados["total"]} gols !')