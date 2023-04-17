#Faça um programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-vespertino ou N-noturno.
#Imprima a mensagem "Bom dia!","Boa tarde!" ou "Boa noite!" ou "Valor inválido",conforme o caso.

print('--- Bem vindo ---')
print('---     ao    ---')
print('---  programa de turno ---')

data_1=str=input('Digite o Turno que você estuda (M , V ou N)\n')

if data_1.upper() == 'M':
    print('Bom dia!')
elif data_1.upper() == 'V':
    print('Boa tarde!')
elif data_1.upper() == 'N':
    print('Boa noite!')
else:
    print('Valor inválido!')
