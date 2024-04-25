    # Uma fruteira está vendendo frutas com a seguinte tabela de preços:

    #                       Até 5 Kg           Acima de 5 Kg
    # Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
    # Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg

    # Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00,
    # receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e
    # a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente. 


print(' ##                  Tabela de preços da fruteria                 ## \n')
print(' ##                                                               ## \n')
print(' ##              Até 5 Kg                        Acima de 5 Kg    ## \n')
print(' ##  Morango   R$ 2,50 por Kg                   R$ 2,20 por Kg    ## \n')
print(' ##  Maçã      R$ 1,80 por Kg                   R$ 1,50 por Kg    ## \n')

fruta = int(input('Selecione a fruta desejada (1) para Maçã e (2) para Morango\n'))

match fruta:
    case 1:
        print('Selecionado Maçã \n')
        peso = float(input('Agora escreva o peso desejado : \n'))
        if peso <= 5 :
            pFinal = 1.80 * peso 
            print('Maça: \n')
            print('Peso: ', peso ,'Kg\n')
            print('Total: R$ {:.2f}'  .format(pFinal),'\n')
        elif peso > 5:
            pFinal = 1.50 * peso
            print('Maça: \n')
            print('Peso: ', peso ,'Kg\n')
            print('Total: R$ {:.2f}'  .format(pFinal),'\n')
    case 2:
        print('Selecionado Morango \n')
        peso = float(input('Agora escreva o peso desejado : \n'))
        if peso <= 5 :
            pFinal = 2.50 * peso 
            print('Morango: \n')
            print('Peso: ', peso ,'Kg\n')
            print('Total: R$ {:.2f}'  .format(pFinal),'\n')
        elif peso > 5:
            pFinal = 2.20 * peso
            print('Morango: \n')
            print('Peso: ', peso ,' Kg\n')
            print('Total: R$ {:.2f}'  .format(pFinal),'\n')
    case _:
        print('Valor inválido, selecione 1 ou 2')
