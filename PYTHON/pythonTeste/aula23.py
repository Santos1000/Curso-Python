'''try:                        # TRATAMENTO DE ERRO geral (há uma lista de Excptions Python)
    a = int(input('Numerador:'))
    b = int(input('Denominador'))
    r = a / b
except Exception as erro:
    print(f'O problema encontrado é {erro.__class__}')
else:
    print(f'O resultado pe {r:.1f}')
finally:
    print(f'Volte sempre, obrigado!')'''

try:                        # TRATAMENTO DE ERRO por classe
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou.')
except (ZeroDivisionError):
    print('Não é possível dividir um número por zero!')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}')
else:
    print(f'O resultado pe {r:.1f}')
finally:
    print(f'Volte sempre, obrigado!')
