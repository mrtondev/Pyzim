#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês,
# sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# A  salário bruto.
# B  quanto pagou ao INSS.
# C  quanto pagou ao sindicato.
# D  o salário líquido.

print(' Programa de contagem de salário e os percentuais descontados')
hora=float(input('Quanto vc ganha por hora?\n'))
quant=int(input('Informe a quantidade de horas trabalhadas no mês: \n'))
sal=float

sal=(hora*quant)

inss=(sal/100)*8
ir=(sal/100)*11
sind=(sal/100)*5
liquid=(sal-sind-ir-inss)




print('Seu salário bruto é de  {:.1f}' .format(sal), 'R$')
print('Descontos:')
print('Inss:(8%) ',inss, 'R$')
print('Imposto de renda:(11%) ',ir, 'R$')
print('Sindicato:(5%) ',sind, 'R$')
print('Salário líquido: {:.1f}'.format(liquid), 'R$')
print('Pode chorar :)')
