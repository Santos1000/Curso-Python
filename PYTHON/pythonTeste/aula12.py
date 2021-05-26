nome = str(input('Qual e seu nome?')).capitalize()
if nome == 'Barbara' :
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Sue nome e bem popular no Brasil.')
else:
    print('Seu nome e norma.')
print('Tenha um bom dia {}{}{}!'.format('\033[;34;0m',nome ,'\033[;34;0m'))
