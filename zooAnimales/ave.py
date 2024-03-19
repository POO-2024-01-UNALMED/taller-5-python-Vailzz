import zooAnimales.animal as animal

class Ave(animal.Animal):
        
    halcones : int = 0
    aguilas : int = 0
    listado : list = []
    
    
    def __init__(self, nombre: str | None = None, edad: int | None = None, habitat: str | None = None, genero: str | None = None, color_pluma : str | None = None) -> None:
        super().__init__(nombre, edad, habitat, genero)
        self._color_pluma = color_pluma
        Ave.listado.append(self)
    
    
    def movimiento(self) -> str:
        return "volar"
    
    
    @classmethod
    def crearHalcon(cls, nombre : str, edad : int, genero : str):
        cls.halcones += 1
        nuevo_Halcon = Ave(nombre, edad, "montanas",genero,"cafe glorioso")
        return nuevo_Halcon
    
    @classmethod
    def crearAguila(cls, nombre : str, edad : int, genero : str):
        cls.aguilas += 1
        nueva_Aguila = Ave(nombre, edad, "montanas",genero,"blanco y amarillo")
        return nueva_Aguila

    
    def getColorPlumas(self) -> str:
        return self._color_pluma
    

    def setColorPlumas(self, color_pluma: str) -> None:
        self._color_pluma = color_pluma
    
    @classmethod
    def get_total_halcones(cls) -> int:
        return cls.halcones
    
    @classmethod
    def get_total_aguilas(cls) -> int:
        return cls.aguilas
    
    @classmethod
    def get_total_animales(cls) -> int:
        return len(cls.listado)
    
    pass

