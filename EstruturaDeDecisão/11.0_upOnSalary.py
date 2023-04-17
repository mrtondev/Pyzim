#Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
#salários até R$ 280,00 (incluindo) : aumento de 20%
#salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
#o salário antes do reajuste;
#o percentual de aumento aplicado;
#o valor do aumento;
#o novo salário, após o aumento. 

print('--- Bem-vindo ---')
print('====== Ao =======')
print('                  ')
print('****** Programa de cálculo de aumento de salário *****')

sal1=float(input('Lançe o valor do seu salário: \n'))


if sal1<=280:
    aumento=(sal1*20)/100
    novoSal=(aumento + sal1)
    
    print('Salário anterior: {:.2f}' .format(sal1))
    print('Aumento de 20% ===', aumento, 'BRL')
    print('Novo salário: {:.2f}' .format(novoSal))

elif (sal1 >280) and ( sal1 < 700):
    aumento = (sal1*15)/100
    novoSal = (sal1+aumento)
    
    print('Salário anterior:{:.2f}'.format(sal1) )
    print('Aumento de 15% ===', aumento, 'BRL')
    print('Novo salário :{:.2f}' .format(novoSal))
elif (sal1 > 700) and (sal1 < 1500):
    aumento = (sal1/10)
    novoSal = (sal1+aumento)
    
    print('Salário anterior:{:.2f}'.format(sal1) )
    print('Aumento de 10% ===', aumento, 'BRL')
    print('Novo salário :{:.2f}' .format(novoSal))
elif sal1>1500:
    aumento = ((sal1*5)/100)
    novoSal = (sal1+aumento)

    print('Antigo salário: {:.2f}'.format(sal1))
    print('Aumento de 5% ===' , aumento, 'BRL')
    print('Novo salário:{:.2f}' .format(novoSal))
else:
    print('ERRO, NÃO FOI POSSÍVEL CALCULAR SEU AUMENTO')