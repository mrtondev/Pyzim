#Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao 
#longo de um semestre, e calcule a sua média. 
#A atribuição de conceitos obedece à tabela abaixo: 

#O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a 
#mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E. 


print('Programa de conceito de média')

print('Você precisará digitar duas notas para obter o resultado da média')

not1=float(input('Insira a primeira nota: \n'))

not2=float(input('Insira a segunda nota: \n'))

media=(not1+not2)/2

if media <=4.0:

    print('Nota1:', not1)
    print('Nota2:', not2)
    print('Média:', media)
    print('Conceito: E')
    print('Reprovado')

elif (media >= 4.1) and (media <= 6.0):

    print('Nota1:',not1)
    print('Nota2:', not2)
    print('Média:', media)
    print('Conceito: D')
    print('Aprovado') 

elif (media >= 6.1) and (media <= 7.4):

    print('Nota1:',not1)
    print('Nota2:', not2)
    print('Média:', media)
    print('Conceito: C')
    print('Aprovado')

elif (media >= 7.5) and (media <= 8.9):

    print('Nota1:',not1)
    print('Nota2:', not2)
    print('Média:', media)
    print('Conceito: B')
    print('Aprovado')

elif (media >= 9) and (media <= 10):

    print('Nota1:',not1)
    print('Nota2:', not2)
    print('Média:', media)
    print('Conceito: A')
    print('Aprovado') 
 


