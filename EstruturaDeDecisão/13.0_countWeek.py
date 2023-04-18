# Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.),
# se digitar outro valor deve aparecer valor inválido.

print(' [[[[[[[[[[ Bem- vindo ]]]]]]]]]]')
print('((((((((((((((((((((( ao )))))))))))))))))))))')
print(' {{{{{{{{{{{{{{{{{{{{{ Programa de dias da semana }}}}}}}}}}}}}}}}}}}}}')



print('Digite um número para um dia da semana (De 1 a 7)')
print('Caso digite alguma coisa fora disso ocorrerá 404')
print('..................................................')

day=int(input('Insira o número agora: \n'))

if (day == 1):
    print('1-Domingo')
elif (day == 2):
    print('2-Segunda')
elif (day == 3):
    print('3-Terça')
elif (day == 4):
    print('4-Quarta')
elif (day == 5):
    print('5-Quinta')
elif (day == 6):
    print('6-Sexta')
elif (day == 7):
    print('7-Sábado')    
else:
    print('404 NOT FOUND')