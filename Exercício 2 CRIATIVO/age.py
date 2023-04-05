#Faça um programa que peça o nome e a data de nascimento do usuário, separado data mes e ano, então mostre quantos anos e meses a pessoa tem de vida

import datetime

atual = datetime.datetime.now()

print('------ BEM VINDO ------\n')
print('------ AO ------\n')
print('------ PROGRAMA DE IDADE --------\n')
name = str(input('DIGITE SEU NOME: \n'))
dia = int(input('AGORA O DIA QUE VOCÊ NASCEU:\n'))
mes = int(input('O MES DO SEU NASCIMENTO: \n'))
ano = int(input('FINALIZE COM SEU ANO DE NASCIMENTO: \n'))

resD = atual.day - dia
resM = atual.month - mes
resA = atual.year - ano


print('--RESULTADO--')
print('NOME:', name)
print('--IDADE ATUAL--')
print('ANOS:', resA)
print('MESES:', resM)
print('DIAS:', resD)
