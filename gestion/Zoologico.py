class Zoologico:
    def __init__(self, nombre, ubicacion, zonas):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.zonas = zonas
    
    def agregarZonas(self, zona):
        self.zonas.append(zona)
    
    def cantidadTotalAnimales(self):
        cantidad = 0
        for zona in self.zonas:
            cantidad += zona.cantidadAnimales()
        return cantidad
