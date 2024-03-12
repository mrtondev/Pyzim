# Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas. 
# As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais.
# O programa não deve se preocupar com a quantidade de notas existentes na máquina.

#     Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
#     Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1

#aprimorando para o valor real afim de aumentar o desafio , foram adicionados os valores de cedulas de 20 e 2 reais

print('Programa de caixa eletrônico \n')

print('Notas disponíveis : 2 , 5 , 10, 20 , 50 e 100 \n')

ced = 100

valorTotal = 0
totalCed = 0

print('O valor mínimo para saque é de 10 reais \n')
print('O valor máximo de saque é de 600 reais \n')

valor=int(input('Digite o valor para sacar:  \n'))

total = valor    

while  True:
    if valor > 10 and valor < 600:    
        if total >= ced:
            total -= ced
            totalCed += 1
        else:
            if totalCed > 0:
                print('Total de', totalCed , 'cédulas de R$' , ced)
            if ced == 100:
                ced = 50
            if ced == 50:
                ced = 20
            elif ced == 20:
                ced = 10
            elif ced == 10:
                ced = 2
            elif ced == 2:
                ced  = 1
            totalCed = 0
            if total == 0:
                break
            
    elif valor > 600:
        print('Valor acima do limite de saque')
        break
    elif valor < 10:
        print('Valor abaixo do limite de saque')
        break        
print('Obrigado e volte sempre :)')