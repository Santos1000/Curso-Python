print('Veja as vogais das seguintes palavras:')
palavras = ('PRENDER', 'CORAÇAO', 'LINGUAGE', 'GRATIS', 'PYTHON',
            'PRATICAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO', 'ESTUDAR')
for p in palavras:
    print(f'Na palavra {p.upper()} temos', end=' ')
    for letra in p:
        if letra.lower() in 'aáéãeiou':
            print(letra, end=' ')