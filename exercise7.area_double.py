#Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
print(' Bem vindo ao calculador de àrea de quadrado')
print(' Após o cálculo da àrea será mostrado o dobro do valor')
lado= float(input('Informe o valor de um lado do quadrado:(em centímetros) \n'))
area = (lado*lado*2)
print('A àrea do quadrado é :{:.1f}' .format(area) ,'cm²')
