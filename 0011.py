larg = float(input('largura da parede: '))
alt = float(input('altura da parede: '))

a = larg * alt

print('Sua parede tem a dimensão de {} x {} e sua area é de {}m'.format(larg, alt, a))

t = a / 2
print('Para pintar essa parede voce precisara de {}L de tinta'.format(t))


