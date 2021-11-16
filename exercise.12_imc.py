#Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: 
#(72.7*altura) - 58

print(' Calculador de IMC ')
alt=float(input('Insira a sua altura:  '))

imc=(72.7*alt)-58

print('Seu peso ideal é:{:.0f}'.format(imc),'kg' )