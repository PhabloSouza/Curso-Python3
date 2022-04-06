#print('Veja quantos dolares você pode comprar.')
#var1 = int(input('Informe o valor: '))
#var2 = var1+5.23
#print('Com {} você poderá comprar {} dólares.'.format(var1, var2))

#Desafio proposto na aula 07 do curso de python.
# crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quanto dolares ela pode comprar.
#não consegui fazer esse exercicio

#RESOLUÇÃO DO DESAFIO 6

real = float(input('Quanto dinheiro você tem na carteira? R$:  '))
dolar = real / 5.25
euro = real / 5.94
print('Dolar hoje: US$ 5,25')
print('Euro hoje: € 5.94')
print('Com R${:.2f} você pode comprar US${:.2f}'.format(real, dolar))
print('Com R${:.2f} você pode comprar €{:.2f}'.format(real, euro))