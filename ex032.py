from  datetime import  date
ano = int(input('Digite um ano ou 0 para ano atual: '))
if ano == 0:
    ano = date.today().year
if (ano % 400) == 0:
    print('{} Foi um ano Bissexto'.format(ano))

else:
     print('{} Nao é um ano  bissexto!'.format(ano))


