velo = float(input('Digite a velocidade:'))
if velo > 80:
    print('Multado! Voce excedeu o limite de velocidade que e 80km/h')
    multa = (velo-80) * 7
    print('Você deve pagar uma multa de R${:.2f}!'.format(multa))

print('Bom dia! Dirija com segurança!')
