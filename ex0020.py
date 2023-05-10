import random
nome1 = input('Primeiro aluno:')
nome2 = input('Segundo aluno: ')
nome3 = input('Terceiro nome: ')
nome4 = input('Quarto nome: ')
list = [nome1, nome2, nome3, nome4]
random.shuffle(list)
print('Os alunos sorteados sao:')
print(list)
