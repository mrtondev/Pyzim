#Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. 
#O resultado da operação deve ser acompanhado de uma frase que diga se o número é:

    # par ou ímpar;
    # positivo ou negativo;
    # inteiro ou decimal. 

print('Bem-vindo ao programa \n')
print('1- Ele irá efetuar a leitura de dois números \n')
print('2- Em seguida ele irá lhe perguntar qual operação você realizará \n')
print('3- O resultado informará se o resultado é : \n')
print('4- Par ou ímpar\n')
print('5- Inteiro ou decimal\n')

firstN = float(input('Digite o primeiro número: \n'))
secondN = float(input('Agora o segundo número: \n'))

operador = str(input('Digite o operador matemático ( + / - * )\n'))

res = float

match operador:
    case '+':
        res = firstN + secondN
    case '-':
        res = firstN - secondN
    case '*':
        res = firstN * secondN
    case '/':
        res = firstN / secondN
    case _:
        print('Operador inválido')


print('Resultado:\n')
print(res ,'\n')
if res.is_integer() == True:    
    print('É inteiro \n')
    if res % 2 == 0:
        print('É par \n')
    else:
        print('É ímpar \n')
else:
    print('É real \n')

if res > 0:
    print('É positivo \n')
else:
    print('É negativo \n')
