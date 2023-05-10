s = float(input('Seu salario atual: '))

r = s + (s * 15 / 100)

print('Seu salario atual e de R${:.2f} '
      '\ne foi alterado para R${:.2f} '
      '\napos o recebimento de 15%.'.format(s, r))
