# Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto. 


print('Verificador de ano bissextos \n')
ano=int(input('Digite um número correspondete a um ano \n'))


res = ano/4

if int(res) == res  :
    print('O ano de {:.0f}'.format(ano), 'é bissexto')

else:
    print('O ano de {:.0f}'.format(ano) , 'não é bissexto')