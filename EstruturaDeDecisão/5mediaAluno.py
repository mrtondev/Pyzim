#Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
# A mensagem "aprovado" se a média alcançada for maior ou igual a 7
# A mensagem "reprovado" se a média for menor que 7
# A mensagem "Aprovado com distinção" se a média for igual a 10


print(' --- Programa de cálculo de média ---')

name=str(input('Digite seu nome: \n'))
nota1=float(input('Digite a primeira nota: \n'))
nota2=float(input('Digite a segunda nota: \n'))

media = (nota1+nota2)/2

print(name)
if media == 10:
    print('Média: ', media)
    print('Aprovado com distinção')
elif media >= 7 < 9.9:
    print('Média: ',media)
    print('Aprovado')
elif media < 7:
    print('Média: ', media)
    print('Reprovado')
else:
    print('Error')
