## Actividad - Excepciones


#Localiza el error en el siguiente bloque de c�digo. Crea una funci�n con la excepci�n 
#para evitar que el programa se bloquee y adem�s explica en un mensaje al usuario la causa y/o soluci�n:

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

