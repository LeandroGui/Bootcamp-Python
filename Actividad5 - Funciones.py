## Actividad 5 - Funciones  ##

# 1_Realiza una funci�n llamada area_rectangulo() que devuelva el �rea del rect�ngulo
# a partir de una base y una altura. Calcula el �rea de un rect�ngulo de 15 de base y 10 de altura.

# Ayuda: El �rea de un rect�ngulo se obtiene al multiplicar la base por la altura.

def area_rectangulo(base, altura):
    return base * altura

area_rectangulo(15,10)


# 2_Realiza una funci�n llamada area_circulo() que devuelva el �rea de un c�rculo a partir de un radio. 
# Calcula el �rea de un c�rculo de 5 de radio.

# Ayuda: El �rea de un c�rculo se obtiene al elevar el radio a dos y multiplicando el resultado por el n�mero pi. Puedes utilizar el valor 3.14159 como pi 
# o importarlo del m�dulo math.

import math
#print(math.pi)

def area_circulo(radio):
    return math.pi * radio**2

area_circulo(5)


# 3_Realiza una funci�n llamada relacion() que a partir de dos n�meros cumpla lo siguiente:

# 1. Si el primer n�mero es mayor que el segundo, debe devolver 1.
# 2. Si el primer n�mero es menor que el segundo, debe devolver -1.
# 3. Si ambos n�meros son iguales, debe devolver un 0.

# Comprueba la relacion entre los numeros: '5 y 10', '10 y 5', '5 y 5'

def relacion(n1,n2):
    if n1 > n2:
        return 1
    elif n1 < n2:
        return -1
    else:
        return 0

relacion(5,10)


# 4_Realiza una funci�n llamada intermedio() que a partir de dos n�meros, 
# devuelva su punto intermedio:

# Ayuda: El n�mero intermedio de dos n�meros corresponde a la suma 
# de los dos n�meros dividida entre 2.

# Comprueba el punto intermedio entre -12 y 24

def intermedio(num1,num2):
    return (num1 + num2) / 2 

intermedio(-12,24)


# 5_Realiz� una funci�n llamada recortar() que reciba tres par�metros. 
# El primero es el n�mero a recortar, el segundo es el l�mite inferior 
# y el tercero el l�mite superior. La funci�n tendr� que cumplir lo siguiente:

# 1.	Devolver el l�mite inferior si el n�mero es menor que �ste.
# 2.	Devolver el l�mite superior si el n�mero es mayor que �ste.
# 3.	Devolver el n�mero sin cambios si no se supera ning�n l�mite.

# Comprueba el resultado de recortar 15 entre los limites 0 y 10

def recortar(numero, limite_inf, limite_sup):
    if numero < limite_inf :
        return limite_inf
    elif numero > limite_sup :
        return limite_sup
    else:
        return numero

recortar(15, 0, 10)


# 6_Realiza una funci�n separar() que tome una lista de n�meros enteros 
# y devuelva dos listas ordenadas. La primera con los n�meros pares, 
# y la segunda con los n�meros impares:

# Ayuda: Para ordenar una lista autom�ticamente puedes usar el m�todo .sort()

def separar(lista):
    pares = []
    impares = []
    for i in lista:
        if i % 2 == 0:
            pares.append(i)
        else:
            impares.append(i)
    
    pares.sort()
    impares.sort()

    print(pares)
    print(impares)

separar([6,5,2,1,7])





