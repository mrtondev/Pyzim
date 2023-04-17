#Faça um programa que verifica se uma letra digitada é "F" ou "M"
#Conforme a letra escrever F - Feminino, M - Masculino,sexo inválido


print('--- Bem vindo ao programa de verificação de sexo ---')
print('---Digite M ou F --- ')

a=str(input())

if a.upper() ==  'M':
    print('Masculino')
elif a.upper() ==  'F':
    print('Feminino')
else:
    print('Sexo inválido')
