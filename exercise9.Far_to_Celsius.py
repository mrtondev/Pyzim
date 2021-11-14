#Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius

print('--------Conversor de Fahrenheit para Celsius------ ')
F=int(input('Informe o valor da temperatura em Fahrenheit \n'))
C = 5 * ((F-32) / 9)

print('São {:.0f}' .format(C),'° Celsius')