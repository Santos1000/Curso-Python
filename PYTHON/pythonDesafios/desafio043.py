peso = float(input('Qual e o seu peso (kg)?'))
altura = float(input('Qual e a sua altura (m)?'))
imc = peso / (altura **2)
print(f'Seu IMC e :{imc:.1f}')
if imc <= 18.8:
    print('Voce esta abaixo do peso !')
elif 18.8 < imc < 25:
    print('Voce esta no peso IDEAL! Parabens!')
elif 25.1 < imc <= 30:
    print('Voce esta com sobrepeso')
elif 30.1 < imc <= 40:
    print('Voce esta OBESO!! Cuidado!')
elif imc > 40:
    print('Voce esta com Obesidade Morbida!')
