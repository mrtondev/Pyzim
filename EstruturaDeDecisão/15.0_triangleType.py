#Faça um Programa que peça os 3 lados de um triângulo.
#O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um 
#triângulo, se o mesmo é: equilátero, isósceles ou escaleno. 

print('¨¨¨¨¨Programa¨¨¨¨')
print('   @@@@ de @@@')
print(' !!!! Tipos de triângulo !!!')

s1=float(input('Digite um lado do triângulo: \n'))
s2=float(input('Digite o segundo lado do triângulo: \n'))
s3=float(input('Agora o terceiro lado: \n'))

if (s1 == s2) and (s2 == s3):
        print('Triângulo:')
        print('Equilátero')
elif ((s1 == s2) and s2 != s3 and s1 != s3) or ((s1 == s3) and s2 != s1 and s2 != s3):
        print('Triângulo')
        print('Isósceles')
else:
        print('Triângulo')
        print('Escaleno')