#João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar
# o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior 
# que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar 
# uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso.
# Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar.
# Imprima os dados do programa com as mensagens adequadas.

print('Programa para o Jõao Pescador')
print('Controle de peso')
peso=float(input('Insira a quantidade (em Kg) de peixes \n'))
multa=float


if (peso > 50): 
        excedente=(peso - 50)
        multa=(excedente*4)
        print('A quantidade de peso excedida foi :' ,excedente ,'KG')
        print('Valor da multa foi :{:.0f}'  .format(multa) , 'R$')
else: print('O peso não foi excedente ao limite (50 KG) e não pagará multa')     
