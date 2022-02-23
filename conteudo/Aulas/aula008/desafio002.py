''' Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retângulo.
calcule ae mostre o comprimento da hipotenusa'''

'''co = float(input('Qual é o comprimento do cateto oposto: '))
ca = float(input('Qual é o comprimento do cateto adjacente:'))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hi))'''

import math
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = math.hypot(co , ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))
