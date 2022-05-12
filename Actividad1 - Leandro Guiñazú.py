#Semana 1

#Actividad 1

#Consigna: Crear un programa para calcular la nota final del estudiante en base a dos exámenes, 
#los exámenes cuentan con un porcentaje distinto de la nota final.

#nota_1 cuenta como el 40% de la nota final
#nota_2 cuenta como el 60% de la nota final

nota_1 = int(input("Ingrese nota 1: "))
nota_2 = int(input("Ingrese nota 2: "))

nota_final = nota_1 * 0.40 + nota_2 * 0.60

print("La nota final es: ",nota_final)