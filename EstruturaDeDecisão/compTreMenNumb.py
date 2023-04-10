#Faça um programa que leia três números e mostre o maior e o menor deles

print('--- Programa que mostra números comparados ---')

a=float(input('Digite o primeiro número: \n'))
b=float(input('Digite o segundo número: \n'))
c=float(input('Digite o terceiro número: \n'))

if a>b>c:
    print(a)
    print(c)
elif a<b>c:
    print(b)
    print(c)
elif a<b<c:
    print(c)
    print(a)
else:
    print('error')
