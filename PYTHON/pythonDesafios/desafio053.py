frase = str(input('Digite uma frase:')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
inverso = junto[::-1]
'''for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]'''
print(f'O inverso da {junto} e {inverso}.')
if inverso == junto:
    print('Temos um palindromo')
else:
    print('nao temos um palindromo!')
