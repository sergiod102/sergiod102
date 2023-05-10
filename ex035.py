print('-='*20)
print('Verificador de Triangulos')
print('-='*20)
a = float(input('Digite um lado: '))
b = float(input('Digite mais um lado: '))
c = float(input('Digite um outro lado: '))

if a < c + b and b < a + c and c < a + b:
    print('É um triangulo')
else:
    print('Não e um triangulo!')
#Se a soma de dois lados quaisquer for maior
# que o terceiro lado, ok, é triângulo.

