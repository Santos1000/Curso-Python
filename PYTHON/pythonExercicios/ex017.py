import math
ca = float(input('Qual o valor do cateto adjacente?'))
co = float(input('Qual o valor do cateto oposto?'))
h = math.hypot(co, ca)
print(f'O valor da hipotenusa sera:{h:.2f}m')

