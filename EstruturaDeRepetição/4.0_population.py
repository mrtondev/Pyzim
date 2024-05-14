# Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e 
# que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e 
# escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento. 
import time


pA = 80000

pB = 200000

anos = 0


cresA =  3

cresB = 1.5

print('População inicial do País A: 80000 \n')
print('População inicial do País B: 200000 \n')

while pA <= pB:
    pA += pA * (cresA/100)
    pB += pB * (cresB/100)
    anos += 1
    print('Ano:', anos)
    print('População A:', pA)
    print('População B:', pB)
    time.sleep(1.5)

print('Em', anos , 'anos , a População do País A superou a do País B \n')