
from zooAnimales.animal import Animal
class Pez(Animal):
    salmones=0
    bacalaos=0
    _listado=[]

    def __init__(self,nombre=None,edad=0,habitat=None,genero=None,colorEscamas=None,cantidadAletas=0):
        super().__init__(nombre,edad,habitat,genero)
        self._colorEscamas=colorEscamas
        self._cantidadAletas=cantidadAletas
        Pez._listado.append(self)
        Animal.totalAnimales+=1
    
    def movimiento():
        return "nadar"
    
    @classmethod
    def crearSalmon(cls,nombre,edad,genero,):
        cls.salmones+=1
        return Pez(nombre,edad,"oceano",genero,"rojo",6)
    @classmethod
    def crearBacalao(cls,nombre,edad,genero,):
        cls.bacalaos+=1
        return Pez(nombre,edad,"oceano",genero,"gris",6)

    @classmethod
    def cantidadPeces(cls):
        return len(cls._listado)
    
    def getColorEscamas(self):
        return self._colorEscamas
    def setColorEscamas(self, colorEscamas):
        self._colorEscamas=colorEscamas
    def getCantidadAletas(self):
        return self._cantidadAletas
    def setCantidadAletas(self, cantidadAletas):
        self._cantidadAletas=cantidadAletas
    
    @classmethod
    def getListado(cls):
        return cls._listado
    @classmethod
    def setListado(cls,listado):
        cls._listado=[]
        cls._listado=listado
