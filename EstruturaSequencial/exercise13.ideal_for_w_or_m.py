#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7

print('Calculadora de peso ideal ')
name=str(input('Insira seu nome: '))
alt=float(input('Agora sua altura: '))
sex=str(input('Qual seu sexo? (h ou m) \n'))
peso=int

if (sex == 'h') :
    peso=(72.7*alt) - 58
elif(sex == 'm'):
    peso=(62.1*alt) -44.7
else:print('Dados incorretos !')    
    
print('Nome:', name )
print('Altura:', alt )
print('Peso ideal:{:.1f}' .format(peso))        