# Faça um programa que faça 5 perguntas para uma pessoa sobre um crime.
#  As perguntas são:

#     "Telefonou para a vítima?"
#     "Esteve no local do crime?"
#     "Mora perto da vítima?"
#     "Devia para a vítima?"
#     "Já trabalhou com a vítima?" 
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
# entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente". 

import time

print('Olá, tenho umas questões para você : \n')
print('Resonda elas você será listado como: \n')
print('1- Inocente\n')
print('2- Suspeito\n')
print('3- Cúmplice\n')
print('4- Assassino\n')

count =0

resp=(input('Você telefonou para a vítima? (S/N) \n'))


if resp.upper() == 'S':
    count = count+1

resp=(input('Esteve perto do local do crime? (S/N) \n'))


if resp.upper() == 'S':
    count = count+1

resp =(input('Mora perto da vítima? (S/N) \n'))


if resp.upper() == 'S':
    count = count+1

resp =input('Devia para a vítima? (S/N) \n')


if resp.upper() == 'S':
    count = count+1

resp = input('Já trabalhou com a vítima? (S/N)\n')


if resp.upper() == 'S':
    count = count+1


print('Carregando resultado... \n')

time.sleep(5)

print('Número de respostas positivas para o crime ...\n')
print(count)

if count < 2:
    print('Inocente\n')
elif count == 3 or count == 4:
    print('Suspeito\n')
elif count == 5:
    print('Culpado\n')

print('Fim do programa')