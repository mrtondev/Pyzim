#Faça um programa para uma loja de tintas
# O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00
# Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

cover=3
full=18
price=80

area=float(input('Informe o tamanho da àrea a ser pintada (em mt²): '))

lts=(area/cover)
needed= int(lts/full)
if(lts%full !=0):
    needed +=1
    
    totalprice= full*needed
    print('Necessita de :',needed, ' latas de tinta')
    print('Preço total  R$: {:.2f}'.format(totalprice))

