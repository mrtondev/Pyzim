# Faça um programa que leia um nome de usuário e a sua senha e 
# não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

from getpass import getpass

comparador = False

print('Verificar de login \n')
print('Será solicitado para você criar um usuário e uma senha \n')
print('Porém a senha não pode ser igual ao usuário \n')

while comparador == False:

    user =str(input('Por favor digite o usuário \n'))
    senha = getpass('Agora digite sua senha \n')
    if user != senha:
        comparador == True
        print('Ok, tudo certo \n')
        break
    else:
        print('Erro \n')
        print('Usuário e senha são idênticos, por favor, crie de forma diferente \n')
        comparador == False


