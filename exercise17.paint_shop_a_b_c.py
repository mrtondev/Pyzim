#Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
 #Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, 
 #que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
 
 #Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
 # A)comprar apenas latas de 18 litros
 # B)comprar apenas galões de 3,6 litros
 # C)misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.


print('Programa de cálculo de uso de tinta')

area=float(input('Digite a àrea a ser pintada (em mts²) \n'))

lts=(area/6) * 1.1

totalata = (lts/18)

totalgala= (lts/3.6)
    
precolata = (totalata*80)
precogalao = (totalgala*25)

misturaslatas= (lts/18)
misuragaloes=((lts-misturaslatas * 18) /3.6)

if ((lts -(misturaslatas * 18)% 3.6 !=0)):
    misuragaloes +=1
    totalmistura = (misturaslatas * 80 ) + (misuragaloes * 25)
print (' Pintando apenas com latas de tinta serão necessárias : {:.0f} '  .format(totalata) , 'e o valor total seria de R$: {:.2f}' .format(precolata)) #a
print (' Pintando apenas com galões de tinta serão necessárias : {:.0f}'  .format(totalgala) , 'e o valor total seria de R$: {:.2f}' .format(precogalao)) #b
print (' Pintando com mistura de galões e latas serão necessárias: Latas: {:.0f}' .format(misturaslatas), 'Galões: {:.0f}'.format(misuragaloes)) #c
print (' O valor total seria de R$: {:.2f}'.format(totalmistura))
 