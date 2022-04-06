'''
O professor quer sortear um dos seus 4 alunos para apagar o quadro.
Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido
'''

''' Passo 1 - importar a biblioteca ramdom'''
import random
#pode tbm utilizar o from para importar somente o choice

''' Passo 4 - Nomes da lista'''
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))

''' Passo 3 - criando a lista de alunos '''
lista = [n1, n2, n3 ,n4]
escolhido = random.choice(lista)

'''Passo 4 - Mostrar o aluno sorteado'''
print('O aluno escolhido foi {}'.format(escolhido))