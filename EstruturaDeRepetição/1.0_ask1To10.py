#Faça um programa que peça uma nota, entre zero e dez.
#  Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido


valido = False

while valido == False:
    nota=float(input('Digite uma nota entre um e 10: \n'))
    if nota < 11 and nota > 0:
        valido = True
        print('Valor válido')
        break
    else:
        print('Valor inválido, tente novamente \n')
        valido = False