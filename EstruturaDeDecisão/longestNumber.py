#Faça um programa que peça dois números e imprima o maior deles

print('--- Bem-vindo ---')
print('--- ao ---')
print('--- Programa de comparação de número ---')

a=int(input('Digite um número: \n'))
b=int(input('Digite outro número: \n'))

if a > b :
    print(a,' É o maior número')
elif b > a:
    print(b, 'É o maior número')
elif a == b:
    print('Os números são iguais')
else:
    print('ERROR')
