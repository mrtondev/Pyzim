#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre
#a) o produto do dobro do primeiro com metade do segundo
#b) a soma do triplo do primeiro com o terceiro.
#c) o terceiro elevado ao cubo.

print('Será solicitado 2 números inteiros e um real:')
inteiro1=int(input('Primeiro número inteiro:'))
inteiro2=int(input('Segundo número intero:'))
real=float(input('Número real:'))

a=(inteiro1*2)+(inteiro2/2)
b=(inteiro1*3)+real
c=(real*real*real)

print('Resultado do a:' ,a)
print('Resultado do b:' ,b)
print('Resultado do c:',c)

