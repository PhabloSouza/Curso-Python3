'''
O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos.
Faça um programa que leia o nome dos quatros alunos e mostre a ordem dos sorteados.
'''

'''Passo 1 - importa a biblioteca ou from'''
import random

'''Passo 2 - digitar os nomes dos alunos'''
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))

'''Passo 3 - criar lista de alunos e implementar o ramdom'''
lista = [n1, n2, n3, n4]
random.shuffle(lista)

'''Passo 4 - mostrar a lista em ordem aleatória criada'''
print('A ordem de apresentação será:\n{}'.format(lista))