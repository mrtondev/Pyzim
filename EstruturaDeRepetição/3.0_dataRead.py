# Faça um programa que leia e valide as seguintes informações:

#     Nome: maior que 3 caracteres;
#     Idade: entre 0 e 150;
#     Salário: maior que zero;
#     Sexo: 'f' ou 'm';
#     Estado Civil: 's', 'c', 'v', 'd'; 

import time


print('Digite as informações solicitadas para realização do cadastro \n')



validade = False
foward = False

while validade == False:
    while foward == False:

        name = str(input('Seu nome: \n'))
        contDigitos = name.__len__()

        if contDigitos > 3:
            foward = True
            print('\n')
            print('Validado.... \n')
            print('\n')
            print('Próximo.... \n')
            print('\n')
        else:
            foward = False
            print('\n')
            print('Erro: \n')
            print('\n')
            print('O nome precisa ter pelo menos 3 caracteres : \n')
            print('\n')
    foward = False
    while foward == False:
        age = int(input('Sua idade: \n'))
        if age < 150 and age > 0:
            foward = True
            print('\n')
            print('Validado... \n')
            print('\n')
            print('Próximo.... \n')
            print('\n')
        else:
            foward = False
            print('\n')
            print('Idade precisa ser entre 0 e 150 anos')
            print('\n')
    foward = False
    while foward == False:
        sal = float(input('Seu salário: \n'))
        if sal > 0 :
            foward = True
            print('\n')
            print('Validado.... \n')
            print('\n')
            print('Próximo.... \n')
            print('\n')
        else:
            foward = False
            print('\n')
            print('Erro \n')
            print('\n')
            print('Salário não pode ser 0 ou menor \n')
            print('\n')
    foward = False
    while foward == False:
        sex = str(input('Sexo: (M) ou (F)'))
        if sex.upper() == 'M' or sex.upper == 'F':
            foward = True
            print('\n')
            print('Validado... \n')
            print('\n')
            print('Seguinte ... \n')
            print('\n')
        else:
            foward = False
            print('\n')
            print('Erro \n')
            print('\n')
            print('M ou F \n')
            print('\n')
    foward = False
    while foward == False:
        civEst = str(input('Estado civil: (S)olteir(o)a , (Casado(a) , Viuvo(a), divorciado(a)) \n '))
        if civEst.upper() == 'S' or civEst.upper() == 'C' or civEst.upper() == 'V' or civEst.upper() == 'D':
            foward = True
            print('\n')
            print('Validado ... \n')
            print('\n')
        else:
            print('\n')
            print('Erro \n')
            print('\n')
            print('Escolha uma das opções: (S)olteir(o)a , (Casado(a) , Viuvo(a), divorciado(a)) \n')
            print('\n')
    validade = True

print('Carregando resultados... \n')
print('\n')
time.sleep(2)
print('#### Dados cadastrados ####')
print('Nome:', name)
print('Idade:',age)
print('Salário: R$ {:.2f}' .format(sal))
print('Sexo:', sex.upper())
print('Estado Civil:' , civEst.upper())
