# Um posto está vendendo combustíveis com a seguinte tabela de descontos:

#     Álcool:
#     até 20 litros, desconto de 3% por litro
#     acima de 20 litros, desconto de 5% por litro
#     Gasolina:
#     até 20 litros, desconto de 4% por litro
#     acima de 20 litros, desconto de 6% por litro Escreva um algoritmo que leia o número de litros vendidos,
#     o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina),
#     calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90. 

print('Programa de Descontos do posto: \n')

print('Tabela de descontos: \n')
print('#########################################################\n')
print('#   Álcool: R$ 1,90 o litro                             #\n')
print('#  Acima de 20 litros, desconto de 5% por litro         #\n')
print('#*******************************************************#\n')
print('#  Gasolina: R$ 2,50 o litro                            #\n')
print('#  Até 20 litros, desconto de 4% por litro              #\n')
print('#  Acima de 20 litros, desconto de 6% por litro         #\n')
print('#########################################################\n')


print(' Tipos de Combustível \n')

print('A - álcool \n')
print('G - gasolina \n')
resp=str(input('Selecione o combustível desejado \n'))

if resp.upper() == 'A':
    print('Selecionado Álcool \n')
    quant=float(input('Agora insira a quantidade de litros : \n'))
    if quant > 20:
       print('Adicionado ' , quant ,'litros de Álcool\n')
       print('Você obteve 5% de desconto\n')
       valorOri =  quant * 1.90
       Desc = (valorOri/100)*5
       print('Valor original: R$ {:.2f}' .format(valorOri), '\n')
       print('Valor descontado: R$ {:.2f}' .format(Desc),'\n')
       print('Valor final c/ desconto: R${:.2f}' .format(valorOri - Desc)),'\n'
    else:
       print('Adicionado ' , quant ,'litros de Álcool\n')
       valorOri =  quant * 1.90
       print('Valor final :{:.2f}' .format(valorOri) )
elif resp.upper() == 'G':
    print('Selecionado Gasolina\n')
    quant=float(input('Agora insira a quantidade de litros : \n'))
    if quant <= 20:
       print('Adicionado ' , quant ,'litros de Gasolina\n')
       print('Você obteve 4% de desconto\n')
       valorOri =  quant * 1.90
       Desc = (valorOri / 100) * 4
       print('Valor original:R$ {:.2f}' .format(valorOri), '\n')
       print('Valor descontado:R$ {:.2f}' .format(Desc),'\n')
       print('Valor final c/ desconto:R${:.2f}' .format(valorOri - Desc)),'\n'
    elif quant >20 :
       print('Adicionado ' , quant ,'litros de Gasolina\n')
       print('Você obteve 6% de desconto\n')
       valorOri =  quant * 1.90
       Desc = (valorOri / 100) * 6
       print('Valor original:R$ {:.2f}' .format(valorOri), '\n')
       print('Valor descontado:R$ {:.2f}' .format(Desc),'\n')
       print('Valor final c/ desconto: R${:.2f}' .format(valorOri - Desc),'\n')
          
 
    
else:
 print('Tipo de combustível inválido, selecione (A)lcool ou (G)asolina')


 