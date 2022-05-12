#Crear una herencia múltiple, trabajando con Mamífero, Cetáceo, AnimalMarino. 
#Realizar la herencia múltiple respetando este diagrama de clases.


class Mamifero:
  
    # Constructor de la clase
    def __init__(self, cant_mamas=0 , esperanza_de_vida=0):

        #Atributo de la instancia
        self.__cant_mamas = cant_mamas
        self.__esperanza_de_vida = esperanza_de_vida

    #Metodos get - lo puedo visibilizar
    def get_cant_mamas(self):
        return self.__cant_mamas

    def get_esperanza_de_vida(self):
        return self.__esperanza_de_vida

    #Metodos set - lo pudo modificar
    def set_cant_mamas(self, cant_mamas):
        self.__cant_mamas = cant_mamas

    #Metodos
    def mamar(self):
        print("Esta mamando")

    def nacer(self):
        print("Ha nacido")

mamifero1 = Mamifero(5, 50)

print(f"cantidad de mamas: {mamifero1.get_cant_mamas()}")
print(f"Esperanza de vida {mamifero1.get_esperanza_de_vida()} años")
print("***************************************************************")

class Animal_Marino:
  
    # Constructor de la clase
    def __init__(self, tiene_branqueas=True, especie=""):

        #Atributo de la instancia
        self.__tiene_branqueas = tiene_branqueas
        self.__especie = especie

    #Metodos get - lo puedo visibilizar
    def get_tiene_branqueas(self):
        return self.__tiene_branqueas

    def get_especie(self):
        return self.__especie

    #Metodos
    def nadar(self):
        print("Esta nadando")

animal_marino1 = Animal_Marino(True,"Calamar")

print(f"Tiene branqueas? {animal_marino1.get_tiene_branqueas()}")
print(f"Especie: {animal_marino1.get_especie()}")
print("***************************************************************")

class Cetaceo(Mamifero, Animal_Marino):
  
    # Constructor de la clase
    def __init__(self, notas="", vive_en="", peso=0 ):

        #Atributo de la instancia
        self.__notas = notas
        self.__vive_en = vive_en
        self.__peso = peso

    #Metodos get - lo puedo visibilizar
    def get_notas(self):
        return self.__notas

    def get_vive_en(self):
        return self.__vive_en

    def get_peso(self):
        return self.__peso

cetaceo1 = Cetaceo("Prueba", "Villa Nueva" , 50)

cetaceo1.nacer()

print(f"Notas:  {cetaceo1.get_notas()}")
print(f"Vive en: {cetaceo1.get_vive_en()}")
print(f"Su peso es: {cetaceo1.get_peso()} kilos")

cetaceo1.nadar()