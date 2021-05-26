def ficha(jog='<desconhecido>', gol = 0):
    print( f'O(A) jogador(a) {jog} fez {gol} gol(s) no campeonato.' )


j = str(input('Nome do jogador(a): '))
g = str(input('Número de gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if j.strip() == '':
    ficha(gol= g)
else:
    ficha(j , g)
