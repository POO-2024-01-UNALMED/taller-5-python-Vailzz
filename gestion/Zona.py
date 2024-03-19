class Zona:
    def __init__(self, nombre, zoo, animales):
        self.nombre = nombre
        self.zoo = zoo
        self.animales = animales
    
    def agregarAnimales(self, animal):
        self.animales.append(animal)
    
    def cantidadAnimales(self):
        return len(self.animales)
