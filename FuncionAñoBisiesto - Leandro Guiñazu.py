# Consigna: Realizar una funcion llamada año_bisiesto:

# 1.Recibira un año por parametro.
# 2.Imprimirá "El año" ,anio, "es bisiesto" si el año es bisiesto.
# 3.Imprimirá "El año" ,anio, "no es bisiesto" si el año no es bisiesto.
# 4.Si se ingresa algo que no sea numero debe indicar que se ingrese un número.

# Información a tener en cuenta al realizar el entregable:

# Se recuerda que los años bisiestos son múltiplos de 4, 
# pero los múltiplos de 100 no lo son, aunque los múltiplos de 400 sí. 
# Estos son algunos ejemplos de posibles respuestas: 2012 es bisiesto, 
# 2010 no es bisiesto, 2000 es bisiesto, 1900 no es bisiesto.


def año_bisiesto(anio):
 
    if isinstance(anio,int):
                
        if anio % 4 == 0 and anio % 100 != 0:
            print("El año",anio,"es bisiesto")
        elif anio % 400 == 0:
            print("El año",anio,"es bisiesto")
        else:
            print("El año",anio,"no es bisiesto")

    else:
        
        print("Debe ingresar un numero!!!")
                    
año_bisiesto("Hola mundo")


