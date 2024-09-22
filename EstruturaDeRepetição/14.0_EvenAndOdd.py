#Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.
contador = 1
gavetaImpar =[]
gavetaPar=[]
while contador < 10:
   print('Digite o ', contador, 'número:')
   recebe=int(input(""))
   if recebe % 2 == 0:
      gavetaPar.append(recebe)
   else:
      gavetaImpar.append(recebe)
      
   contador +=1
print("Números Pares: ", gavetaPar)
print("Números Ímpares: ", gavetaImpar)
