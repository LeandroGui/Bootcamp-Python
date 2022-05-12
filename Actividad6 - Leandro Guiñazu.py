#Crea una clase llamada Cuenta que tendr� los siguientes atributos: 
#titular (que es una persona) y cantidad (puede tener decimales). 
#El titular ser� obligatorio y la cantidad es opcional. 
#Construye los siguientes m�todos para la clase:

# * Un constructor. 
# * mostrar(): Muestra los datos de la cuenta. 
# * ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, no se har� nada. 
# * retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en n�meros rojos.

class Cuenta:

    #Constructor de la clase donde los datos pueden estar vacios.
    def __init__(self, titular="", cantidad=0):


        #Atributos de la instancia
        self.titular = titular      #Publico
        self.__cantidad = cantidad  #Privado

    #Metodos
    def mostrar(self):
        return "Datos de la cuenta\n"+"Titular: "+self.titular+" - Cantidad: "+str(self.__cantidad)

    def ingresar(self, cantidad):
        if cantidad > 0:
            self.__cantidad += cantidad
            return cantidad

    def retirar(self, cantidad):
        if cantidad > 0:
            self.__cantidad -= cantidad 
            return cantidad


#Objeto
cuenta1 = Cuenta("Leandro Gui�azu", 100000.50)


print(cuenta1.mostrar()) #Consulto la cuenta
print("Ingresar dinero a la cuenta: ",cuenta1.ingresar(-10000))

print(cuenta1.mostrar()) 

print("Retirar dinero de la cuenta: ", cuenta1.retirar(110000))
print(cuenta1.mostrar())

