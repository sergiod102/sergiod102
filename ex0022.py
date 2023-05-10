nome = input("Digite seu nome complete: ")
print(nome.upper())
print(nome.lower())

nnome = len(nome.replace(" ",""))
nomed = nome.split()
numdi = len(nomed[0])
print('O seu nome tem  letras {} e o seu primeiro nome tem {} letras'.format(nnome, numdi))


#O método strip apenas remove os espaços no começo e fim da string.
#Neste caso, o ideal é usar o método replace,
#que irá substituir todos os espaços por um caractere escolhido
# (ou nenhum caractere neste caso), da seguinte forma.