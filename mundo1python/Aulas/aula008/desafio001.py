''' Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.

import math
num = float(input('Digite um valor: '))
print('O valor digitado foi {} a sua porção inteira é {}'.format(num, math.trunc(num)))'''

num = float(input('Digite o valor: '))
print('O valor digitado foi {} e a porção inteira é {}'.format(num, int(num)))
