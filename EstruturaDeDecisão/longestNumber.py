#Faça um programa que peça dois números e imprima o maior deles

print('--- Bem-vindo ---')
print('--- ao ---')
print('--- Programa de comparação de número ---')

a=float(input('Digite um número: \n'))
b=float(input('Digite outro número: \n'))

if a > b :
    print('O maior número é: ',a)
elif a < b :
    print('O maior número é: ', b)
elif a == b:
    print('Os números são iguais')
else: 
    print('ERRO 404 NÃO ENCONTRADO')
