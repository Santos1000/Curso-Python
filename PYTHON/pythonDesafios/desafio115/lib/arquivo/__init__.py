from desafio115.lib.interface import *


def arqExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArq(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Hoouve um Erro na criação do arquivo')
    else:
        print(f'Arquivo {nome} criado com sucesso.')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler arquivo')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            print(f'{dado[0]:<30}{dado[1]:>3}anos')
    finally:
        a.close()


def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at')   # a --> arquivo
    except:
        print('Houve um Erro na abertura do arquivo')
    else:
        try:
            a.write(f'{nome},{idade}')
        except:
            print('Houve um ERRO na hora de escrever os dados.')
        else:
            a.close()
