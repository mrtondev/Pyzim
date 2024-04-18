#Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento. 

print('Programa de verifcador de números \n')

print('Este programa tem o objetivo de verificar se o valor informado é: \n')

print('Inteiro \n')

print(' ou  \n')

print('Real \n')


numb =float(input('Digite um número: \n'))



print('O número escolhido é: \n' , numb)

if numb.is_integer() == True:
    print('É inteiro \n')
    
else:
    print('É real\n')


