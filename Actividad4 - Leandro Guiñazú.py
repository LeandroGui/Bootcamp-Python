#Ejercicio 1 -

#Escribir un programa que lea dos números por teclado y permita elegir entre 4
#opciones en un menu:

# 1.	Mostrar una suma de los dos números.
# 2.	Mostrar una resta de los dos números (el primero menos el segundo).
# 3.	Mostrar una multiplicación de los dos números.
# 4.	Si elige esta opción se interrumpirá la impresión del menú y el programa finalizará.
# 5.	En caso de no introducir una opción válida, el programa informará de que no es correcta.


ingresar_numero1 = int(input("Ingrese numero 1: "))
ingresar_numero2 = int(input("Ingrese numero 2: "))

print("Menu de opciones:")
print("1_Suma de los dos números.\n2_Resta de los dos números (el primero menos el segundo).\n3_Multiplicación de los dos números.\n4_Salir")

num = 1

while num != 0:
    ingrese_opcion = int(input("Ingrese numero de opcion: "))
    if ingrese_opcion > 0 and ingrese_opcion < 2:
        print(f"La suma de {ingresar_numero1} + {ingresar_numero2} es: ", ingresar_numero1 + ingresar_numero2)
    elif ingrese_opcion > 1 and ingrese_opcion < 3:
        print(f"La resta de {ingresar_numero1} - {ingresar_numero2} es: ", ingresar_numero1 - ingresar_numero2)
    elif ingrese_opcion > 2 and ingrese_opcion < 4:
        print(f"La multiplicacion de {ingresar_numero1} * {ingresar_numero2} es: ", ingresar_numero1 * ingresar_numero2)
    elif ingrese_opcion > 3 and ingrese_opcion < 5:
        print("Programa finalizado")
        break

    else:
      print("El numero ingresado de opcion no es correcta, vuelva a intentarlo") 

#Programas realizados sin bloque de excepciones.


#Ejercicio 2 - 

#Escribí un programa que lea un número impar por teclado. Si el usuario no introduce 
#un número impar, debe repetirse el proceso hasta que lo introduzca correctamente.

numero = 1

while numero != 0:
    ingresar_num = int(input("Ingrese un numero impar: "))
    par_impar = ingresar_num % 2
    if par_impar == 0:
        print("Debe ingresar un numero impar!!!")

    else:
        print("El numero ingresado impar es: ", ingresar_num)
        break


#Ejercicio 3 - 

#Sumar los numeros enteros impares del 0 al 100.

lista_a_sumar = sum(list(range(1,101,2)))

print("La suma de los numeros impares del 0 al 100 es: ",lista_a_sumar)


#Ejercicio 4 - 

#Escribir un programa que pida al usuario cuantos numeros quiere introducir.
#Luego lee todos los numeros y realiza una media aritmética.

print("Indique al sistema cuantos numeros se deben introducir")

cant_numeros = int(input("Ingrese cantidad de numeros: "))

cont = 0

for elemento in range (cant_numeros):
    ingrese_num = int(input(f"Ingrese numero {elemento +1} :"))
    cont += ingrese_num

media_aritmetica = cont / cant_numeros    
print("La media aritmetica es: ", media_aritmetica)


#Ejercicio 5 -

#Escribir un programa que pida al usuario un numero entero del 0 al 9, y que 
#mientras el numero no sea correcto se repita el proceso. Luego debe comprobar
#si el numero se encuentra en la lista de numeros y notificarlo:

numeros = [1, 3 ,6, 9]
print("Numeros en la lista: ",numeros)
n = 1

while n != 0:
    numeros_a_ingresar = int(input("Ingrese un numero entero del 0 al 9: "))
    if numeros_a_ingresar >= 0 and numeros_a_ingresar <= 9:
        for num in numeros:
            if num == numeros_a_ingresar:
                print("El numero se encuentra en la lista")
        break
    else:
        print("Debe ingresar un numero del 0 al 9")


#Ejercicio 6 -

#Utilizando la funcion range() y la conversion a listas genera las siguientes listas:

#?	Todos los números del 0 al 10 [0, 1, 2, ..., 10]
#conversion a lista  
mi_lista_i = list(range(0,11))
print(mi_lista_i)

#?	Todos los números del -10 al 0 [-10, -9, -8, ..., 0]
#conversion a lista
mi_lista_ii = list(range(-10,1))
print(mi_lista_ii)

#?	Todos los números pares del 0 al 20 [0, 2, 4, ..., 20]
#conversion a lista
mi_lista_iii = list(range(0,21,2))
print(mi_lista_iii)

#?	Todos los números impares entre -20 y 0 [-19, -17, -15, ..., -1]
#conversion a lista
mi_lista_iv = list(range(-19,0,2))
print(mi_lista_iv)

#?	Todos los números múltiples de 5 del 0 al 50 [0, 5, 10, ..., 50]
#conversion a lista
mi_lista_v = list(range(0,51,5))
print(mi_lista_v)


#Ejercicio 7 -

#Dadas dos listas, debes generar una tercera con todos los elementos que se
#repiten en ellas, pero no debe repetirse ningun elemento en la nueva lista:

lista_1 = ['h','o','l','a','','m','u','n','d','o']
print("Lista 1: ", lista_1)
lista_2 = ['h','o','l','a','','l','u','n','a']
print("Lista 2: ", lista_2)

lista_3 = []

for letter in lista_1:
    if letter in lista_2 and letter not in lista_3:
        lista_3.append(letter)

print("Lista 3: ",lista_3)

#Otra manera de redactar el ejercicio:
# Dadas dos listas, debes generar otra lista(podes o no usar una cuarta lista) 
# sin repetir ningun elemento.
print("Otra forma de redactar el ejercicio y sus resoluciones")


lista_3_II = lista_1 + lista_2
nueva_lista = []

for i in lista_3_II:
    if i not in nueva_lista:
        nueva_lista.append(i)  

print("Nueva lista: ",nueva_lista)    

#Con list comprehension - comprension de listas
lista_3_III = lista_1 + lista_2

nueva_lista_II = []
[nueva_lista_II.append(i) for i in lista_3_III if i not in nueva_lista_II]
print("Nueva lista II: ", nueva_lista_II)


lista_3_IV = []

for letter in lista_1:
    if (letter in lista_2 and letter not in lista_3_IV) or (letter not in lista_2):
        lista_3_IV.append(letter)

print("Retro: ", lista_3_IV)

