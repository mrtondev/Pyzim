#Faça um programa que leia três números e os exiba de forma descrescente

print('--- Programa de ordem decrescente ---')

data1=float(input('33333333 Digite o primeiro número 33333333 \n'))
data2=float(input('11111111 Digite o segundo número 111111111 \n'))
data3=float(input('........ Digite o terceiro número ..... \n'))

if data1<data2<data3:
    print(data3)
    print(data2)
    print(data1)
elif data3<data2<data1:
    print(data1)
    print(data2)
    print(data3)
elif data3<data1<data2:
    print(data2)
    print(data1)
    print(data3)
elif data2>data1>data3:
    print(data3)
    print(data1)
    print(data2)
elif data1<data3<data2:
    print(data2)
    print(data3)
    print(data1)
elif data2<data3<data1:
    print(data1)
    print(data3)
    print(data2)
else:
    print('ERROR')
