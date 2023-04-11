#Faça um Programa que peça as 4 notas bimestrais e mostre a média.

print(' Bem-vindo à calculadora de média')
name=str(input('Nome:  \n '))
print('Olá aluno, por favor insira as notas dos 4 bimestres para saber seu resultado :)')
nota1=int(input('Valor da primeira nota: \n '))
nota2=int(input('Valor da Segunda nota: \n'))
nota3=int(input('Valor da terceira nota: \n'))
nota4=int(input('Valor da quarta nota: \n'))

result=(nota1+nota2+nota3+nota4)/4

print('Aluno:',name)
print('Nota:',result)

if (result >=5):
    print('Você passou')
else:
    print('Você foi reprovado')