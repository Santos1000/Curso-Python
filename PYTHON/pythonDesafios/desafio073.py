brasil = ('Corintians', 'Palmeiras', 'Santos', 'Gremio', 'Cruzeiro',
          'São Paulo', 'Botafogo')
print('--'*55)
print(f'Lista de times do Brasileirão: {brasil}')
print('--'*55)
print(f'Os cinco primeiros são:{brasil[:5]}')
print(f'Os quatro últimos são:{brasil[-4:]}')
print(f'Os times em ordem alfabetica: {sorted(brasil)}')
print('--'*20)
print(f'O Santos está na {brasil.index("Santos")+1} posição.')

