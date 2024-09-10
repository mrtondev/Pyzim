#Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. 
# Depois modifique o programa para que ele mostre os números um ao lado do outro. 
z=1
nums=[z]

def contadorH(z):
        while z > 0 and z < 20:
             z+=1
             print(z)
             nums.append(z)  
        return
contadorH(z)

print(nums)