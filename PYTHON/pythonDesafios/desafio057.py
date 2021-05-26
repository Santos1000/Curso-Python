sexo = str(input('Digidite (F) ou (M) para indicar se é feminino ou masculino: ')).upper().strip()[0]
while sexo not in 'FMfm':
    sexo = str( input( 'Digidite (F) ou (M) para indicar se é feminino ou masculino: ' ) ).upper().strip()[0]
print('Obrigado! sexo registrado')