dados = dict()
galera = list()
soma = média = 0
while True:
    dados.clear()
    dados['nome'] = str(input('Nome: '))
    dados['sexo'] = str(input('Sexo: ')).strip().upper()
    if dados['sexo'] not in 'FM':
        print( 'ERRO! Responda apena F ou M ' )
        dados['sexo'] = str( input( 'Sexo: ' ) ).strip().upper()
    dados['idade'] = int(input('Idade: '))
    soma += dados['idade']
    resp1 = str(input('Quer continuar [S;N]: ')).strip().upper()
    galera.append(dados.copy())
    if resp1 not in 'SN':
        print('ERRO! Responda apena S ou N ')
        resp1 = str( input( 'Quer continuar [S;N]: ' ) ).strip().upper()
    elif resp1 in 'N':
        break
print(galera)
print('-='*30)
print(f'A) Ao todo temos {len(galera)} pessoa(s) no cadastro.')
média = soma / len(galera)
print(f'B) A média de idade é de {média:5.2f} anos.')
print( f'C) As mulheres cadastradas foram: ',end=' ')
print()
for s in galera:
    if s['sexo'] == 'F':
        print(f'{s["nome"]}',end=' ;')
print()
print(f'D) Lista das pessoas que estão acima da média de idade:')
for s in galera:
    if s['idade'] >= média:
        print('    ', end='')
        for k, v in s.items():
            print(f'{k} = {v} ',end='')
        print()
print('<<ENCERRADO>>')