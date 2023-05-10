nome = str(input('Digite seu nome:')).split()
print('Seu primeiro nome é: {} '.format(nome[0]))
print('E o ultimo:{}'.format(nome[-1]))



# usei .split() para dividir a string on tiver espaço
# assim cada elemento recebe uma numeração
# e usei no .format()[] os colchetes para colocar o numero de cada
# elento sendo o primeiro representado sempre por [0] e o ultimo por
# [-1]