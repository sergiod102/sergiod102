a = int(input('Primeiro: '))
b = int(input('Segundo: '))
c = int(input('Terceiro: '))
# verificando que e menor

menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# verificar maior

maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print('o menor valor digitado foi {}'.format(menor))
print('o maior valor digitado foi {}'.format(maior))
