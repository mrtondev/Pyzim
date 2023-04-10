#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar,sabendo que a decisão é sempre pelo mais barato

print(' 000 Programa de economia 000')
produto1_name=str(input('Informe o nome do primeiro produto: \n'))
produto1_preco=float(input('Informe o valor: \n'))

produto2_name=str(input('Informe o nome do segundo produto: \n'))
produto2_preco=float(input('Informe o valor: \n'))

produto3_name=str(input('Informe o nome do terceiro produto: \n'))
produto3_preco=float(input('Informe o valor: \n'))

if produto1_preco>produto2_preco>produto3_preco:
    print('Compre o ',produto3_name)
elif produto1_preco<produto2_preco>produto3_preco:
    print('Compre o ',produto3_name)
elif produto1_preco<produto2_preco<produto3_preco:
    print('Compre o ', produto1_name)
else:
    print('Compre o ', produto2_name)
