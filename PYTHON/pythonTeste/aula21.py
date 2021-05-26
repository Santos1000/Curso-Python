#interactive HELP PARA FUNÇAO DOS PARAMETROS
'''def contador(i, f, p):
    """

    :param i: início da contagem
    :param f: final da contagem
    :param p: passo da contagem
    :return: sem
    funçao driada pela Bárbara Santos
    """

    c = i
    while c <= f:
        print(f'{c}',end=' ')
        c += p


contador(2, 100, 4)
'''
'''
#PARAMETROS OPCIONAIS
def soma(a = 0, b = 0, c = 0):  #adicione o = 0 para caso o valor na lista não exista
    s = a + b + c
    print(f'A soma vale {s}')


soma( 9, 2)
'''
'''
#ESCOPO DE VARIÁVEIS
  #Variável local
def test():
    x = 8
    print(f'Na função test, n vale {n}')
    print(f'Na função teste, x valoe {x}')


     #Variável global  Programa principal
n = 2
print(f'No programa principal n vale {n}')
teste()
print(f'No programa principal x vale {x}')
 
 '''
#RETORNO DE VALORES  ----> para não ficar repetindo o print com a frase junto, para cada valor.
def somar(a=0 , b=0, c=0):
    s = a+b+c
    return s


r1= somar(2, 3, 5)
r2= somar(1, 7)
r3= somar(4)
print(f'Meus cálculos deram {r1}, {r2} e {r3}.')