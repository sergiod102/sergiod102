frase = str(input('Digite uma frase:')).upper().strip()
print('Quantidade de letras A: {}'.format(frase.count('A')))
print('Qual a sua primeira posição: {}'.format(frase.find('A')+1))
print('A sua ultima posição: {}'.format(frase.rfind('A')+1))
