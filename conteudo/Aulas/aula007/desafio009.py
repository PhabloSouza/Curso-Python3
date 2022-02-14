# Desafio 9 do curso de Python
# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
# Resolução do exercicio

salario = float(input('Digite aqui o salário do funcionário R$'))
aumento = salario + (salario * 15 / 100)
print('O novo salário do funcionário pós aumento de 15% é de R${}.'.format(aumento))

