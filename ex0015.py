dias = int(input('Digite o numero de dias: '))
rodar = float(input('Quantos KM rodados: '))

t = (60 * dias) + (rodar * 0.15)

print('O Valora ser pago e de {:.2f}'.format(t))

