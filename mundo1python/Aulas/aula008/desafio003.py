'''
Faça um programa que leia um angulo qualquer e mostre na tela o valor do senop, cosseno e tangente desse angulo
'''
''' 
from math import radians, sin, cos, tan e remove os math
'''
import math
an = float(input('Digite o ângulo que você deseja: '))
se = math.sin(math.radians(an))
print('O ângulo de {} tem o SENO de {:.2f}'.format(an, se ))
co = math.cos(math.radians(an))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(an, co))
ta = math.tan(math.radians(an))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(an, ta))
