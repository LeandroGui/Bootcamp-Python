#Ejercicio 3

#El siguiente código pretende realizar una media entre 3 números, pero no funciona correctamente. 
#¿Eres capaz de identificar el problema y solucionarlo?

#Respuesta:

numero_1 = 9
numero_2 = 3
numero_3 = 6

media = (numero_1 + numero_2 + numero_3) / 3
print("La nota media es", media)


#Ejercicio 4

#A partir del ejercicio anterior, desarrolla un programa para calcular la nota final. 
#Para ello vamos a suponer que cada número es una nota y que queremos obtener la nota media. 
#Cada nota tiene un valor porcentual:

#La primera nota vale un 15% del total.
#La segunda nota vale un 35% del total.
#La tercera nota vale un 50% del total.

nota_1 = 10
nota_2 = 7
nota_3 = 4

nota_final = (nota_1 * 0.15 + nota_2 * 0.35 + nota_3 * 0.50)
print("La nota final es: ", nota_final)


#Ejercicio 5

#La siguiente matriz (o lista con listas anidadas) debe cumplir una condición: 
#en cada fila el cuarto elemento siempre debe ser el resultado de sumar los tres primeros. 
#¿Eres capaz de modificar las sumas incorrectas utilizando la técnica del slicing?

#Ayuda:  La función llamada sum(lista) devuelve una suma de todos los elementos de la lista

matriz = [ 
    [1, 5, 1],
    [2, 1, 2],
    [3, 0, 1],
    [1, 4, 4]
]
#Una forma de resolver
matriz[0].append(sum(matriz[0]))
matriz[1].append(sum(matriz[1]))
matriz[2].append(sum(matriz[2]))
matriz[3].append(sum(matriz[3]))

print(matriz)

#Otra forma de resolver

matriz_2 = [ 
    [1, 5, 1],
    [2, 1, 2],
    [3, 0, 1],
    [1, 4, 4]
]
matriz_2 = [[1,5,1,sum(matriz_2[0])], 
          [2,1,2,sum(matriz_2[1])], 
          [3,0,1,sum(matriz_2[2])], 
          [1,4,4,sum(matriz_2[3])]
          ]
print(matriz_2)


