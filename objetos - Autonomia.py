class tierra:
    def __init__(self, cant_tierra, fertilizantes, lombrices):
        self.cant_tierra = cant_tierra
        self.fertilizantes = fertilizantes
        self.lombrices = lombrices

    def mas_tamaño(self):
        if self.fertilizantes > 5:
            return planta.TAMAÑO + planta.TAMAÑO * .20

#Creo la clase padre
class planta:

#Self significa el tipo de clase y sirve para poder acceder y modificar los atributos y metodos
    def __init__(self,nombre, CANT_DIAS, TAMAÑO, HIDRATACION, ENERGIA, MAX_ENERGIA, MAX_HIDRATACION, INVENTARIO):

        #cambia los valores que se den aca a la clase principal
        self.nombre = nombre
        self.CANT_DIAS = CANT_DIAS
        self.TAMAÑO = TAMAÑO
        self.HIDRATACION = HIDRATACION
        self.ENERGIA = ENERGIA
        self.MAX_ENERGIA = MAX_ENERGIA
        self.MAX_HIDRATACION = MAX_HIDRATACION
        self.INVENTARIO = INVENTARIO
    def atributos(self):    
        print("La planta es una/un:", self.nombre)
        print("Cantidad de dias:", self.CANT_DIAS, )
        print("Tamaño:", self.TAMAÑO)  
        print("Hidratacion:", self.HIDRATACION)
        print("Energia:", self.ENERGIA)
        print("Max_Hidratacion:", self.MAX_HIDRATACION)
        print("Max_Energia:", self.MAX_ENERGIA)
        print("Inventario:", self.INVENTARIO)

    def existe(self):
        return self.TAMAÑO > 0
    
    def cosechar(self):
        if self.TAMAÑO >= 25:
            self.TAMAÑO = 0 
            self.INVENTARIO += 1
        else:
            self.TAMAÑO < 25
            print("Falta tamaño para cosechar")
    
    def regar(self):
        self.HIDRATACION -= 10 
        self.TAMAÑO += 3
        return self
    
    def energizar(self):
        self.ENERGIA -= 10
        self.TAMAÑO += 3
        return self 

    
#Creo la primera planta
class girasol1(planta):
    def __init__(self, nombre, CANT_DIAS, TAMAÑO, HIDRATACION, ENERGIA, MAX_ENERGIA, MAX_HIDRATACION,INVENTARIO, polen):
        super().__init__(nombre, CANT_DIAS, TAMAÑO, HIDRATACION, ENERGIA, MAX_ENERGIA, MAX_HIDRATACION, INVENTARIO)
        self.polen = polen

    def atributos(self):
        super().atributos()
        print("Cantidad de polen:", self.polen)

    def abejas(self):
        opciones = int(input("Elige un tipo de abeja: (1) Abeja Madre, polen 10 --- (2) Abeja padre, polen 8."))
        if opciones == 1:
            self.polen = 10
        elif opciones == 2:
            self.polen = 8
        else:
            print("Solo tienes dos abejas :(")

    def tamaño(self):
        return self.TAMAÑO + self.polen

#Creo la segunda planta
class flor1(planta):
    def __init__(self, nombre, CANT_DIAS, TAMAÑO, HIDRATACION, ENERGIA, MAX_ENERGIA, MAX_HIDRATACION,INVENTARIO, petalos):
        super().__init__(nombre, CANT_DIAS, TAMAÑO, HIDRATACION, ENERGIA, MAX_ENERGIA, MAX_HIDRATACION, INVENTARIO)
        self.petalos = petalos

    def atributos(self):
        super().atributos()
        print("Cantidad de petalos:", self.petalos)

    def caracoles(self):
        opciones = int(input("Elije tu caracol: (1) Caracol lento, petalos 4 --- (2) Caracol rapido, petalos 1"))
        if opciones == 1:
            self.petalos = 4
        elif opciones == 2:
            self.petalos = 1
        else:
            print("Solo tienes dos caracoles")

    def tamaño(self):
        return self.TAMAÑO + self.petalos * 2

flor = flor1("flor", 0, 0, 50, 50, 100, 100, 0, 0)
girasol = girasol1("girasol", 0, 1, 50, 50, 100, 100, 0, 0)

flor.caracoles()
flor.cosechar()
flor.atributos()

#girasol.abejas()
#girasol.tamaño()
#girasol.atributos()

#girasol.cosechar()