num = int(input('Digite um numero inteiro:'))
print('''Escolha uma das bases para conversao:
[1] converter para BINARIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL''')
opcao = int(input('Escolha sua opcao:'))
if opcao == 1:
    print(f'{num} convertido para BINARIO e igual a {bin(num)}')
elif opcao == 2:
    print(f'{num} convertido para OCTAL e igual a {oct(num)}')
elif opcao == 3:
    print(f'{num} convertido para HEXADECIMAL e igual a {hex(num)}')
else:
    print('ERRO.Digite as opcoes de 1 ao 3 novamente.')
