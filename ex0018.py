from math import radians, sin, cos, tan

a = float(input("Digite o angulo: "))
seno = sin(radians(a))
consseno = cos(radians(a))
tangente = tan(radians(a))
print('Seno {:.2f}, cosseno {:.2f} e tangente {:.2f}'.format(seno, consseno, tangente))
