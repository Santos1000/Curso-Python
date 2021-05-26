from desafio115.lib.interface import *
from desafio115.lib.arquivo import *
from time import sleep


arq = 'Curso em video'

if not arqExiste(arq):
    criarArq(arq)

while True:
    resp = menu(['Cadastrar Pessoas','Listar Pessoas',
                 'Sair do Sistema'])
    if resp == 1:
        # OPÇÃO DE LISTAR UM ARQUIVO
        print(f'{lerArquivo()}')
    elif resp == 2:
        cabeçalho('Novo Cadastro')
        nome = str(input('Nome'))
        idade = leiaInt('Idade')
        cadastras(arq, nome, idade)
    elif resp == 3:
        cabeçalho('Opção 3. Saindo do sistema...')
        break
    else:
        cabeçalho('\033[31mERRO.Digite uma opção válida.\033[m')
    sleep(2)
