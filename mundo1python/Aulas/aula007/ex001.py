n1 = int(input('Digite o valor: '))
n2 = int(input('Outra valor: '))
s = n1+n2
m = n1*n2
d = n1/n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, o produto é {} e a divisão é {:.3f}'.format(s, m, d), end=' ')
print('Divisão inteira {} potencia {}'.format(di, e))