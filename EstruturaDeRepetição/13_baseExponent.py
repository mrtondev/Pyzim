#Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. 
# Não utilize a função de potência da linguagem.

print("*" *10,'Calculador de Potenciação',"*" *10)

base = int(input('Informe a Base: '))
potencia = int(input('Agora o Expoente: '))

gavetaBase = []
contador = 1
res = 1
while contador <= potencia:
    gavetaBase.append(base)
    res *= base
    contador += 1


print(gavetaBase,"=",res)