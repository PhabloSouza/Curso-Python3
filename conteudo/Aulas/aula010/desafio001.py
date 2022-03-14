# Esecreva um programa que faça o compuatdor "pensar" em um número inteiro entre 0 e 5,
# E peça para o usuário tentar descobrir qual foi o número escolhido pelo comptador.
# O programa devetá escrever na tela se o usuário venceu ou perdeu

from random import randint
from time import sleep
computador = randint(0, 5) # Faz o computador "PENSAR"
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? ')) # Jogador tenta advinhar
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(computador, jogador))