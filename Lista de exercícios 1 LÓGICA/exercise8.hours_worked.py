#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
print(' Calculador de salário')
print('Será solicitado o valor de ganho por hora e o número de horas trabalhadas para realizar o cálculo')
ganho=float(input('Ganho por hora trabalhada:'))
horas=int(input('Quantidade de Horas trabalhadas no mês:'))

sal=(ganho*horas)

print('R$ {:.2f}' .format(sal))