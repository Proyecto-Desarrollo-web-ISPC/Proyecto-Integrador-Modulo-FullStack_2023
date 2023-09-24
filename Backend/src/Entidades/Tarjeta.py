class Tarjeta :
    def __init__(self,ID_tarjeta,nombre_tarjeta):
        self._ID_tarjeta = ID_tarjeta
        self._nombre_tarjeta = nombre_tarjeta
        
    @property
    def ID_tarjeta(self):
        return self._ID_tarjeta
    
    @ID_tarjeta.setter
    def ID_tarjeta (self,nuevo_id):
        self._ID_tarjeta = nuevo_id
    
    @property
    def nombre_tarjeta(self):
        return self._nombre_tarjeta
    
    @nombre_tarjeta.setter
    def nombre_tarjeta(self,nuevo_nombre):
        self._nombre_tarjeta = nuevo_nombre
        
    def __str__(self):
        return f"ID_tarjeta : {self.ID_tarjeta}, NOMBRE DE LA TARJETA: {self.nombre_tarjeta}"
    
        