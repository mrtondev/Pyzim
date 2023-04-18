#Faça um programa para o cálculo de uma folha de pagamento, 
#sabendo que os descontos são do Imposto de Renda, 
#que depende do salário bruto (conforme tabela abaixo) e 3% para o 
#Sindicato e que o FGTS corresponde a 11% do Salário Bruto, 
#mas não é descontado (é a empresa que deposita).
# O Salário Líquido corresponde ao Salário Bruto menos os descontos.
# O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.

#    Desconto do IR:
#    Salário Bruto até 900 (inclusive) - isento
#    Salário Bruto até 1500 (inclusive) - desconto de 5%
#    Salário Bruto até 2500 (inclusive) - desconto de 10%
#    Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, 
#    dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade 
#    de hora é 220.


print('----- Bem-vindo -----')
print('&&&&&& ao &&&&&&&&&&&&                ' )
print('Programa de verificação de imposto    |   |')
print('                                      xxxxx ')
print('                                           ')

valHora=float(input('Informe aqui o valor da sua hora de trabalho: \n'))
tempHora=float(input('Agora o número de horas trabalhadas no mês: \n'))

salB= tempHora*valHora

fgts=(salB*11)/100

inss=(salB*10)/100

sind=(salB*3)/100


if salB <= 900 : 
    salL=(((salB-fgts)-inss)-sind)

    print('Você está Isendo do IR')
    print('Salário Bruto: {:.2f}' .format(salB))
    print('++++++ Descontos ++++++')
    print(' Sindicato: 3% :', sind)
    print(' FGTS:     11% :', fgts)
    print(' INSS:     10% :', inss)
    print(' Salário Líquido: {:.2f}' .format(salL))

elif (salB >= 901) and (salB <= 1500):
    
    ir=(salB*5)/100

    salL=((((salB-fgts)-inss)-sind)-ir)

    print('Salário Bruto: {:.2f}' .format(salB))
    print('+++++++ Descontos +++++++')
    print('Imposto de Renda: 5%:',ir)
    print(' Sindicato: 3% :', sind)
    print(' FGTS:     11% :', fgts)
    print(' INSS:     10% :', inss)
    print(' Salário Líquido: {:.2f}' .format(salL))

elif (salB >= 1501) and (salB <= 2500):

    ir=(salB*10)/100

    salL=((((salB-fgts)-inss)-sind)-ir)

    print('Salário Bruto: {:.2f}' .format(salB))
    print('+++++++ Descontos +++++++')
    print('Imposto de Renda: 10%:',ir)
    print(' Sindicato: 3% :', sind)
    print(' FGTS:     11% :', fgts)
    print(' INSS:     10% :', inss)
    print(' Salário Líquido: {:.2f}' .format(salL))
elif salB >= 2501:
    ir=(salB*15)/100

    salL=((((salB-fgts)-inss)-sind)-ir)

    print('Salário Bruto: {:.2f}' .format(salB))
    print('+++++++ Descontos +++++++')
    print('Imposto de Renda: 15%:',ir)
    print(' Sindicato: 3% :', sind)
    print(' FGTS:     11% :', fgts)
    print(' INSS:     10% :', inss)
    print(' Salário Líquido: {:.2f}' .format(salL))

