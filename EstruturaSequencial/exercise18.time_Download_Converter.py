# Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps),
# calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).



print (' Programa de tempo de Download ')

mbs = int(input('Qual o tamanho do arquivo de deseja baixar (MBs)?:'))

speed = int(input(' Qual a sua velocidade de conexão (MBs)?:'))

time = (mbs /(speed / 8))/60

print (' O tempo de Download do seu arquivo é de {:.0f}' .format(time),'minuto(s)' )  

