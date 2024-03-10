#Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida. 

print('Programa verificador de datas: \n')
print('\n')
print('Digite uma data no formato dd/mm/aaaa, se for válida ou não, será informado\n')
dd = int(input("Digite o dia: \n"))
mm = int(input("Digite o mês:  \n"))
aaaa =int(input("Digite o ano: \n"))


if dd < 31 and dd >= 1:
    
    if mm > 1 and  mm <= 12:
        
        if aaaa >= 1 :
            print("Formato de data válido \n")
            print("Data: ", dd,"/",mm,"/",aaaa)
        else:
            print('Formato de data inválido \n')
            print('Ano Inválido ')
            
    else:
        print('Formato de data inválido \n')
        print('Mês Inválido')
else:
    print('Formato de data inválido \n')
    print('Dia Inválido')

     