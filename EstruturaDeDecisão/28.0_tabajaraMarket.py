# O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:

#                           Até 5 Kg           Acima de 5 Kg
#     File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
#     Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
#     Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg

#     Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção,
#     porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara 
#     o cliente receberá ainda um desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e 
#     a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra: tipo e 
#     quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar. 

import time

print('Hipermercado Tabajara\n')
print('\n')
print(' #               Tabela de preços                   #\n')
print(' #              Até 5 kg            Acima de 5 kg   #\n')
print(' # Filé duplo  R$ 5,80 por Kg        R$ 4,90 por Kg #\n')
print(' # Alcatra     R$ 6,80 por Kg        R$ 5,90 por Kg #\n')
print(' # Picanha     R$ 7,80 por Kg        R$ 6,90 por Kg #\n')
print('\n')

print('Escolha a carne em promoção: \n')
print('(F) para Filé Duplo:\n')
print('(A) para Alcatra:\n')
print('(P) para Picanha:\n')
tipoC = str(input('\n'))

match tipoC.upper():

    case 'F':
        print('Selecionado Filé Duplo: \n')
        quant = float(input('Informe a quantidade desejada em Kg (Lembrando que acima de 5 kg cai para R$ 4,90 por Kg) \n'))
        valOri = quant * 5.80
        
        if quant > 5:
            print('Acima de 5 Kg, o preço por Kg sai a R$ 4,90')
            valAtac = quant * 4.90
        else : 
            valAtac = valOri
            
    case 'A':
        print('Selecionado Alcatra: \n')
        quant = float(input('Informe a quantidade desejada em Kg (Lembrando que acima de 5 kg cai para R$ 5,90 por Kg) \n'))
        valOri = quant * 6.80
        if quant > 5:
            print('Acima de 5 Kg, o preço por Kg sai a R$ 5,90')
            valAtac = quant * 5.90
        else : 
            valAtac = valOri
    case 'P':
        print('Selecionado Picanha: \n')
        quant = float(input('Informe a quantidade desejada em Kg (Lembrando que acima de 5 kg cai para R$ 6,90 por Kg) \n'))
        valOri = quant * 7.80
        if quant > 5:
            print('Acima de 5 Kg, o preço por Kg sai a R$ 6,90')
            valAtac = quant * 6.90
        else : 
            valAtac = valOri
            
formaPag = str(input('Qual forma de pagamento ? (C) para cartão Tabajara (com 5% de desconto) , (D) para dinheiro \n'))

print('Carregando ....')

time.sleep(2)

if tipoC.upper() == 'P':
    print('Picanha')
elif tipoC.upper() == 'A':
    print('Alcatra')
elif tipoC.upper() == 'F':
    print('Filé duplo')

print('Valor original: R${:.2f}' .format(valOri))
if quant > 5:
    print('Valor promocional (acima de 5kg): R${:.2f}' .format(valAtac))
else:
    print('Menos de 5 Kg não recebe o valor promocional')
if formaPag.upper() == 'C':
    desc = (valAtac/100) * 5
    print('Desconto de cartão Tabajara (5%): R${:.2f}'  .format(desc)  )
    print('Valor final :R${:.2f}' .format(valAtac))
else:
        print('Valor final :R${:.2f}' .format(valAtac))
