## Actividad 5 - Funciones  ##

# 1_Realiza una función llamada area_rectangulo() que devuelva el área del rectángulo
# a partir de una base y una altura. Calcula el área de un rectángulo de 15 de base y 10 de altura.

# Ayuda: El área de un rectángulo se obtiene al multiplicar la base por la altura.

def area_rectangulo(base, altura):
    return base * altura

area_rectangulo(15,10)


# 2_Realiza una función llamada area_circulo() que devuelva el área de un círculo a partir de un radio. 
# Calcula el área de un círculo de 5 de radio.

# Ayuda: El área de un círculo se obtiene al elevar el radio a dos y multiplicando el resultado por el número pi. Puedes utilizar el valor 3.14159 como pi 
# o importarlo del módulo math.

import math
#print(math.pi)

def area_circulo(radio):
    return math.pi * radio**2

area_circulo(5)


# 3_Realiza una función llamada relacion() que a partir de dos números cumpla lo siguiente:

# 1. Si el primer número es mayor que el segundo, debe devolver 1.
# 2. Si el primer número es menor que el segundo, debe devolver -1.
# 3. Si ambos números son iguales, debe devolver un 0.

# Comprueba la relacion entre los numeros: '5 y 10', '10 y 5', '5 y 5'

def relacion(n1,n2):
    if n1 > n2:
        return 1
    elif n1 < n2:
        return -1
    else:
        return 0

relacion(5,10)


# 4_Realiza una función llamada intermedio() que a partir de dos números, 
# devuelva su punto intermedio:

# Ayuda: El número intermedio de dos números corresponde a la suma 
# de los dos números dividida entre 2.

# Comprueba el punto intermedio entre -12 y 24

def intermedio(num1,num2):
    return (num1 + num2) / 2 

intermedio(-12,24)


# 5_Realizá una función llamada recortar() que reciba tres parámetros. 
# El primero es el número a recortar, el segundo es el límite inferior 
# y el tercero el límite superior. La función tendrá que cumplir lo siguiente:

# 1.	Devolver el límite inferior si el número es menor que éste.
# 2.	Devolver el límite superior si el número es mayor que éste.
# 3.	Devolver el número sin cambios si no se supera ningún límite.

# Comprueba el resultado de recortar 15 entre los limites 0 y 10

def recortar(numero, limite_inf, limite_sup):
    if numero < limite_inf :
        return limite_inf
    elif numero > limite_sup :
        return limite_sup
    else:
        return numero

recortar(15, 0, 10)


# 6_Realiza una función separar() que tome una lista de números enteros 
# y devuelva dos listas ordenadas. La primera con los números pares, 
# y la segunda con los números impares:

# Ayuda: Para ordenar una lista automáticamente puedes usar el método .sort()

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





