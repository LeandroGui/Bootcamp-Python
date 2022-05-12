#Ejercicio 1 -
 
#Escriba un programa que pida dos números enteros y 
# que calcule su división, escribiendo si la división es exacta o no.

num_1 = int(input("Ingrese numero 1: "))
num_2 = int(input("Ingrese numero 2: "))


print("La division entre ",num_1," y ",num_2," es: ", num_1 / num_2)
Div_exacta = num_1 % num_2


if Div_exacta == 0:

   print("La division es exacta")

else:

   print("La division no es exacta")




#Ejercicio 2 -
 
#Escriba un programa que pida tres números y que escriba
#  si son los tres iguales, si hay dos iguales o 
# si son los tres distintos.

n_1 = int(input("Ingrese numero 1: "))
n_2 = int(input("Ingrese numero 2: "))
n_3 = int(input("Ingrese numero 3: "))


if n_1 == n_2 and n_2 == n_3:

   print("Todos los numeros ingresados son iguales")

elif (n_1 == n_2 or n_1 == n_3 or n_2 == n_3) and (n_2 != n_3 or n_2 != n_1):

   print("Hay dos numeros iguales")

else:

   print("Todos los numeros son distintos")