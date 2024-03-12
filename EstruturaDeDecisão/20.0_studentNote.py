# Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar:

#     A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
#     A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
#     A mensagem "Aprovado com Distinção", se a média for igual a 10. 

print('Programa calculador de média \n')

name=str(input('Digite seu nome: \n'))

n1=float(input('Digite a primeira nota: \n'))

n2=float(input('Digite a segunda nota \n'))

n3=float(input('Digite a terceira nota \n'))

mt = ((n1 + n2 + n3)) / 3 

print('Aluno : ', name)
print('Nota 1: ', n1)
print('Nota 2:' , n2)
print('Nota 3:', n3)
print('Média : {:.2f}' .format(mt))

if mt >=  7:
   
    print('Aprovado ...')
else:
    print('Reprovado ...')
