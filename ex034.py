salario = float(input('Digite seu salario:R$ '))
if salario >= 1250:
    c = salario +(salario * 10/100)
    print('Seu salario e superior a R$1250 você recebeu 10%, seu novo salario e de:R${} '.format(c))

else:
    b = salario+ (salario * 15 / 100)
    print('Seu salario e inferior a R$1250 voce recebeu 15%, seu novo salario e de:R${} '.format(b))
