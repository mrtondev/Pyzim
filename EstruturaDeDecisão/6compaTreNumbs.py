#Faça um programa que leia 3 números e mostre o maior deles

print(' --- Programa de comparação de 3 números ---')

a=float(input('Digite o primeiro número: \n'))
b=float(input('Digite o segundo número: \n'))
c=float(input('Digite o terceiro número: \n'))

if a>b>c:
    print(a)
elif a<b<c:
    print(c)
elif a<b>c:
    print(b)
elif a==b==c:
    print('Números iguais')
else:
    print('Error')
