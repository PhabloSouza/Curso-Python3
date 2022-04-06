frase = 'Curso em video python exemplo'

''' Comando para analisar uma frase '''
 frase.find('exemplo')
 'curso' in frase

''' Fatiamento '''
frase[9] ''' Ele identifica dentro da cadeia de caracter o 9'''
frase[9:13] ''' Ele vai pegar a mini cadeia do 9 até o 12, ele para de contar antes do 13 '''
frase[9:21] ''' Ele desconsidera o 21 e vai até o 20 '''
frase[9:21:2] ''' Ele começa no 9 para no 21 e pula de dois em dois '''
frase[:5] ''' Quando omite o inicio ele começa do caracter zero '''
frase[15:] ''' Ele começa do 15 e vai até o final '''
frase[9::3] ''' Ele começa no 9 e vai até o final e pulando de 3 em 3 '''


''' Trasnformação'''
frase.replace('Python','Android') ''' Troca a palavra '''
frase.upper() ''' Tudo maiusculo '''
frase.lower() ''' Tudo minusculo '''
frase.capitalize() ''' Só o primeiro caracter maiusculo'''
frase.title() ''' Transforma as primeiras letras em maiusculo '''
frase.strip() ''' Remove os espaços das extremidades '''
frase.rstrip() ''' Remove os espaços da direita '''
frase.lstrip() ''' Remove os espaços da esquerda '''

''' Divisão '''
frase.split() ''' Cada palavra é colocada dentro de outra lista '''

''' Junção '''
'-'.join(frase) ''' Ele vai juntar toda a cadeia com o - tracinho '''