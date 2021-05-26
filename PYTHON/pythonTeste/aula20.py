'''
def soma(a, b):  #DEF USADO EM APENAS ROTINAS
    s = a + b + 1
    print(s)

# PROGRAMA PRINCIPAL
soma(4, 5)
soma(8, 2)
soma(2, 1)
soma(4, 1)'''

'''
def contador(* núm):
    for valor in núm:
        print(f'{valor} ', end='')
    print('FIM!')
    tam = len(núm)
    print(f'Recebi os valores {núm} e são ao todo {tam} números.')


contador(2, 2, 7)       #TUPLAS
contador(8, 0)
contador(4, 4, 7, 6, 2)'''

'''
def dobra(list):        #DESEMPACOTAMENTO COM LISTA
    pos = 0
    while pos < len(list):
        list[pos] *= 2
        pos += 1


valores = [4, 9, 7, 2, 1, 0]
dobra(valores)
print(valores)'''

def soma(* valores):        #DESEMPACOTAMENTO SEM LISTA
    s = 0
    for elemento in valores:
        s += elemento
    print(f'Somando os valores {valores} temos {s}')


soma(5, 2)
soma(2, 4, 8)
