p = float(input('Preço do produto: '))

s = p -(p * 5 / 100)

print('O valor do produto e R${:.2f} e com descondo de 5% sai por R${:.2f}'.format(p, s))
