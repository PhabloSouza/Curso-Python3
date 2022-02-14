# print('Digite aqui o preço do produto')
# var1 = input('Preço do Produto: ')
# desc = var1-5
# print('O produto com desconto sai por: R${}')

# Desafio 8 da aula 7. Calculo de porcentagem.

# RESOLUÇÃO DO DESAFIO

preco = float(input('Qual é o preço do produto? R$ '))
novo = preco - (preco * 5 / 100)
print("O produto que custava R${}, na promoção com desconto de 5% vai custar R${}.".format(preco, novo))

