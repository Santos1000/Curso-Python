cont = ('zero' ,'um' ,'dois' ,'tres' ,'quatro' ,'cinco' ,'seis' ,
       'sete' ,'oito' ,'nove' ,'dez' ,'onze' ,'doze' ,'treze' ,
       'catorze' ,'quinze' ,'desesseis' ,'desessete' ,'desoito','vinte')
resp =' '
while True:
    numero = int(input(' Digite um número entre 0 e 20: '))
    if 0 <= numero <=20:
        break
    print('Tente novamente', end='.')
print(f'Você digitou o número {cont[numero]}')
resp = ' '
while resp not in "NSsn":
    resp = str( input( 'Quer continuar:[s;n] ' ) ).strip().upper()[0]
if resp == 'N':
    print( '{:-^40}'.format('PROGRAMA ENCERRADO'))

