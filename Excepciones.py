## Actividad - Excepciones


#Localiza el error en el siguiente bloque de código. Crea una función con la excepción 
#para evitar que el programa se bloquee y además explica en un mensaje al usuario la causa y/o solución:

#Resultado = 10/0


def Div_sin_cero(num1,num2):

 while True:

    try:
            
            print("Resultado: ", num1 / num2)
            break
    except:        
            print("No se puede dividir por cero")
            break
    
        
Div_sin_cero(10,0)

