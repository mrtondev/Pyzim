#Faça um Programa que peça um número inteiro e determine se ele é par ou impar. Dica: utilize o operador módulo (resto da divisão). 


dado=int(input('Digite um número inteiro e o programa verificará se ele é par ou ímpar \n'))

if dado % 2 == 0:
    print('Seu número', dado, 'é par')
else:
    print('Seu número ', dado , 'é ìmpar')