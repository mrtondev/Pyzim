#Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit
print('Programa conversor de Celsius em Fahrenheit')
c=int(input('Informe a temperatura em Celsius:'))

f=(c*1.8)+32

print('São {:.0f}' .format(f),'° Fahrenheit')