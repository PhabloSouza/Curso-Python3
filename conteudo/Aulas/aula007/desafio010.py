# Desafio 10 da aula 7
# Escreva um programa que converta uma temperatura digitada em C° e converta para F°
# Resolução do desafio

c = float(input('Informe a temperatura em C: '))
f = 9 * c / 5 + 32
print('A temperaatura de {}C corresponde a {} F!'.format(c, f))