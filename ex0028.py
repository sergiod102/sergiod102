from random import randint
from time import sleep
computador = randint(0, 5) # faz o computador pensar
print('-=-' *20)
print('Vou pensar em um numero entre 0 e 5. Tente adivinhas...')
print('-=-' * 20)
jogador = int(input('Em que numero eu pensei? ')) #jogador tenta adivinhar
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('Parabens voce me venceu!')
else:
    print('Ganhei eu pensei no numero {} e nao no {}!'.format(computador, jogador))