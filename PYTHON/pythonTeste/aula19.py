'''pessoas = {'nome':'Barbara', 'sexo':'feminino', 'idade':28}
print(f'O(A) {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
for k in pessoas.keys():
    print(k)
print()
for v in pessoas.values():
    print(v)
print()
for k, v in pessoas.items():
    print(f'{k} = {v}')
# del.pessoa['sexo']       --> APAGANDO
# pessoas['nome'] = 'leandro'   --> MUDANDO
# pessoas['peso'] = 98      --> ADICIONANDO'''
lista = []
estado = {'uf':'Rio de Janeiro', 'sigla':'RJ'}
estado2 = {'uf':'São Paulo', 'sigla':'SP'}
estado3 = {'uf':'Minas Gerais', 'sigla':'MG'}
lista.append(estado)
lista.append(estado2)
lista.append(estado3)
print(lista)
print(lista[0])
print(lista[1]['uf'])
print(lista[2]['sigla'])

