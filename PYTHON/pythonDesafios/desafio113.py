def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mErro. por favor, digite um número inteiro válido.\033[m')
        except (KeyboardInterrupt):
            print('\033[31mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return n


def leiaFlo(msg):
    while True:
        try:
            n = float(input(msg))
        except Exception as erro:
            print('\033[31mErro. Digite um valor novamente.\033[m')
        except (KeyboardInterrupt):
            print('\033[31mErro.Entrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return n


num1 = leiaInt('Digite um valor inteiro: ')
num2 = leiaFlo('Digite um valor Real: ')
print(f'O valor digitado foi {num1} e {num2}.')