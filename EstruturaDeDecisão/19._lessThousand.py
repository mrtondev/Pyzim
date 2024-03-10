## Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.

    ##Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
    ##326 = 3 centenas, 2 dezenas e 6 unidades
    ##12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16 

entrada=float(input('Digite um número menor que 1000 (mil) \n'))

def  verificador (numero):

    centena = numero // 1 % 10
    dezena = numero // 10 % 10
    unidade = numero // 100 % 10

    print('{:.0f}' .format(centena) ,' Centena(s) {:.0f}'  .format(dezena) , ' Dezena(s) {:.0f}'  .format(unidade),' Unidade(s)')
    
    
    


if entrada < 1000 :

 verificador(entrada)

else :
    print('Sinto muito, seu número é maior que 1000 (mil) \n')
    print('Saindo ...')

  
