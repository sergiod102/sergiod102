cid = str(input('Em que cidade voce nasceu:')).strip()
print(cid[:5].upper() == 'SANTO')


#usei o .strip() para retirar os espacos no comeco e no fim
# e usei .upper() para deixar tudo em maiusculo para nao ter erro
# quando o usuario for digitar o nome em miusculo ou minusculo
# o codigo print(cid[:5] ,eu pego o numero de letras faço a
#contagem para saber quantas letras sao para o programa identificar
