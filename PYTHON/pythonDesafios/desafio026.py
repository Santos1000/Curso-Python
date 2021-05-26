frase = str(input('Digite a frase:')).upper().strip()
print('A primeira letra A aparece: na {} posicao.'.format(frase.find('A')+1))
print('A letra A aparece: {} vezes.'.format(frase.count('A')))
print('A ultima letra A aparece: na {} posicao.'.format(frase.rfind('A')+1))
