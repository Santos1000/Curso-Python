def notas(*n, sit = False):
    """
    :param n: uma ou mais notas de alunos de vários alunos
    :param sit: valor opcional, adicionar preferencia no programa principal
    :return: dicionário com as notas da turma
    """
   r = dict()
   r['total'] = len(n)
   r['maior'] = max(n)
   r['menor'] = min(n)
   r['média'] = sum(n)/len(n)
   if sit:
       if r['média'] >=7:
           r['situação'] = 'BOA'
       elif r['média'] <= 5:
           r['situação'] = 'RAZOÁVEL'
       else:
           r['situação'] = 'RUIM'
   return r
print('A maior nota foi ')



resp = notas(5.5 , 3.5, 10, 6.5, 10, sit = True)
print(resp)
help(notas)