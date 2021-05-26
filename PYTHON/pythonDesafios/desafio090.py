
''' DEU CERTO PORÉM AS CHAVES APARECEM , UTILIZAR FOR
nom = str(input('Nome:'))
media = float(input(f'Média de {nom}:'))
lista = []
dic = {'nome':{nom}, 'media': {media} }
if media >= 7:
    sit = 'Aprovado'
else:
    sit = 'Reprovado'
dic['situaçao'] = sit
lista.append(dic)
print('--'*30)
print(f'Nome é igual a {lista[0]["nome"]} ')
print(f'Média é igual a {lista[0]["media"]}')
print(f'A situação final é {lista[0]["situaçao"]}')'''

aluno = dict()
aluno['nome'] = str(input('Nome:'))
aluno['média'] = float(input(f'Média do {aluno["nome"]}:'))
if aluno['média'] >= 7:
    aluno['situaçao'] = 'Aprovado'
elif 5 <= aluno['média'] < 7:
    aluno['situaçao'] = 'Recuperação'
elif aluno['média'] < 5:
    aluno['situaçao'] = 'Reprovado'
else:
    aluno['situaçao'] = 'Valor inválido'
print('=='*15)
for k, v in aluno.items():
    print(f'{k} é {v}.')