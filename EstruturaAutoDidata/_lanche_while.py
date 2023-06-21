#Boot 

print('######################')
print('#                    #')
print('#  Iniciando...      #')
print('#  Programa de       #')
print('#  Auto-atendimento  #')
print('#                    #')
print('#  Teste             #')
print('#                    #')
print('######################')
print('\n')
#Cardápio
print('#####################################################################################')
print('#                                     Cardápio                                      #')
print('#                                                                                   #')
print('#  N°1: Hambúrguer    Preço: R$ 4,00       | N°2: X-burguer        Preço: R$ 5,00   #')
print('#  N°3: X-Picanha     Preço: R$ 8,00       | N°4: X-Tudo           Preço: R$ 10,00  #')
print('#  N°5: Batata-Frita  Preço: R$ 5,00       | N°6: Batata c/ bacon  Preço: R$ 6,00   #')
print('#  N°7: Guaravita     Preço: R$ 2,00       | N°8: Coca-cola 600ml  Preço: R$ 8,00   #')
print('#                                                                                   #')
print('#####################################################################################')
print('\n')
print('\n')

ped=int(input('Faça seu pedido \n'))
conf=str
qH=0
qXB=0
qXP=0
qXT=0
qBT=0
qBC=0
qG=0
qC=0
val_Ped=0
val_total=0

#pedido
while True:

        match ped:

            case 1:
                print('\n')
                print('Hambúrguer   Preço: R$ 4,00 \n')
                qtd=int(input('Qual quantidade? \n'))
                qH += qtd  
                val_Ped = qtd*4.00
                val_total += val_Ped
                print('Adicionado: R$ {:.2f} '.format(val_Ped))

            case 2:
                print('\n')
                print('X-búrguer   Preço: R$ 5,00 \n')
                qtd=int(input('Qual quantidade? \n'))
                qXB += qtd  
                val_Ped = qtd*5.00
                val_total += val_Ped
                print('Adicionado: R$ {:.2f} '.format(val_Ped))
            
            case 3:
                print('\n')
                print('X-Picanha   Preço: R$ 8,00 \n')
                qtd=int(input('Qual quantidade? \n'))
                qXP += qtd  
                val_Ped = qtd*8.00
                val_total += val_Ped
                print('Adicionado: R$ {:.2f} '.format(val_Ped))
            
            case 4:
                print('\n')
                print('X-Tudo   Preço: R$ 10,00 \n')
                qtd=int(input('Qual quantidade? \n'))
                qXT += qtd  
                val_Ped = qtd*10.00
                val_total += val_Ped
                print('Adicionado: R$ {:.2f} '.format(val_Ped))
            
            case 5:
                print('\n')
                print('Batata-Frita   Preço: R$ 5,00 \n')
                qtd=int(input('Qual quantidade? \n'))
                qBT += qtd  
                val_Ped = qtd*5.00
                val_total += val_Ped
                print('Adicionado: R$ {:.2f} '.format(val_Ped))

            case 6:
                print('\n')
                print('Batata frita C/ Bacon   Preço: R$ 6,00 \n')
                qtd=int(input('Qual quantidade? \n'))
                qBC += qtd  
                val_Ped = qtd*6.00
                val_total += val_Ped
                print('Adicionado: R$ {:.2f} '.format(val_Ped))
            
            case 7:
                print('\n')
                print('Guaravita   Preço: R$ 2,00 \n')
                qtd=int(input('Qual quantidade? \n'))
                qG += qtd  
                val_Ped = qtd*2.00
                val_total += val_Ped
                print('Adicionado: R$ {:.2f} '.format(val_Ped))

            case 8:
                print('\n')
                print('Coca-cola 600 ml   Preço: R$ 8,00 \n')
                qtd=int(input('Qual quantidade? \n'))
                qC += qtd  
                val_Ped = qtd*8.00
                val_total += val_Ped
                print('Adicionado: R$ {:.2f} '.format(val_Ped))
            
            case _:
                print('Erro 404 \n')
                print('Não encontrado \n')
                print('Digite o número de outro item \n')
                ped=input('\n')
#loop   

        print('\n')
        print('Valor Atual: R$ {:.2f}' .format(val_total) )        
        print('\n')
        print('Deseja adicionar algo ao seu pedido? \n')
        conf=input('( S PARA RETORNAR AO MENU   ||  N PARA FINALIZAR O PEDIDO ) \n')
        print('\n')
        if conf.upper() == 'N':
#nota 
            print('Finalizando pedido... \n')
            if qH != 0:
                print('\n')
                print('Hambúrguer: ')
                print('Quantidade:  ', qH)
                print('\n')
            else:{}    
            if qXB != 0:
                print('X-búrguer: ')
                print('Quantidade:  ', qXB)
                print('\n')
            else:{}
            if qXP != 0:
                print('X-Picanha: ')
                print('Quantidade:  ', qXP)
                print('\n')
            else:{}
            if qXT != 0:
                print('X-Tudo: ')
                print('Quantidade:  ', qXT)
                print('\n')
            else:{}
            if qBT != 0:
                print('Batata-Frita: ')
                print('Quantidade:  ', qBT)
                print('\n')
            else:{}    
            if qBC != 0:
                print('Batata-Frita c/ Bacon: ')
                print('Quantidade:  ',  qBC )
                print('\n')
            else:{}    
            if qG != 0:
                print('Guaravita: ')
                print('Quantidade:  ', qG)
                print('\n')
            else:{}    
            if qC != 0:
                print('Coca-cola 600 ml: ')
                print('Quantidade:  ', qC)
                print('\n')
            else:{}
            break
        elif conf.upper() == 'S' :
            print('#####################################################################################')
            print('#                                     Cardápio                                      #')
            print('#                                                                                   #')
            print('#  N°1: Hambúrguer    Preço: R$ 4,00       | N°2: X-burguer        Preço: R$ 5,00   #')
            print('#  N°3: X-Picanha     Preço: R$ 8,00       | N°4: X-Tudo           Preço: R$ 10,00  #')
            print('#  N°5: Batata-Frita  Preço: R$ 5,00       | N°6: Batata c/ bacon  Preço: R$ 6,00   #')
            print('#  N°7: Guaravita     Preço: R$ 2,00       | N°8: Coca-cola 600ml  Preço: R$ 8,00   #')
            print('#                                                                                   #')
            print('#####################################################################################')
            print('\n')
            print('Digite o número de outro item ')
            ped=int(input('\n'))

   
#fim do pedido
    
 
print('Total:  R$: {:.2f}' .format(val_total))