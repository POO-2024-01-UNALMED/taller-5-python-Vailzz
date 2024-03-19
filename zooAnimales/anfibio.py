import zooAnimales.animal as animal

class Anfibio(animal.Animal):

    ranas : int = 0
    salamandras : int = 0
    listado : list = []
    
    
    def __init__(self, nombre: str | None = None, edad: int | None = None, habitat: str | None = None, genero: str | None = None, color_piel : str | None = None, venenoso : bool | None = None) -> None:
        super().__init__(nombre, edad, habitat, genero)
        self._color_piel = color_piel
        self._venenoso = venenoso
        Anfibio.listado.append(self)
    
    
    def movimiento(self) -> str:
        return "saltar"
    
    @classmethod
    def crearRana(cls, nombre : str, edad : int, genero : str):
        cls.ranas += 1
        nueva_Rana = Anfibio(nombre, edad, "selva",genero,"rojo",True)
        return nueva_Rana
    
    @classmethod
    def crearSalamandra(cls, nombre : str, edad : int, genero : str):
        cls.salamandras += 1
        nueva_Salamandra = Anfibio(nombre, edad, "selva",genero,"negro y amarillo",False)
        return nueva_Salamandra


    def getColorPiel(self) -> str | None:
        return self._color_piel
    
    def setColorPiel(self, color_piel: str) -> None:
        self._color_piel = color_piel
    
    def isVenenoso(self) -> bool | None:
        return self._venenoso
    
    def setVenenoso(self, venenoso: bool) -> None:
        self._venenoso = venenoso

    @classmethod
    def get_total_rana(cls) -> int:
        return cls.ranas
    
    @classmethod
    def get_total_salamandra(cls) -> int:
        return cls.salamandras
    
    @classmethod
    def get_total_animales(cls) -> int:
        return len(cls.listado)
    
    pass
