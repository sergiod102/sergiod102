#num =int(input('Informe um numero:'))
#u = num // 1 % 10
#d = num // 10 % 10
#c = num // 100 % 10
#m = num // 1000 % 10
#print('analisar o numero {}'.format(num))
#print('Unidade:{}'.format(u))
#print('Dezena:{}'.format(d))
#print('Centena:{}'.format(c))
#print('Milhar{}'.format(m))



num = input('Digite um numero de 0 a 9999:')
num = (f'{num:0>4}')
print(f'unidade:{num[3]}\nDezena: {num[2]}\nCentena: {num[1]}\nMilhar: {num[0]}')