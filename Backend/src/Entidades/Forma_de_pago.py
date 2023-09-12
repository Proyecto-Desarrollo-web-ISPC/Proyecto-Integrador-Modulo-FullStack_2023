
class Forma_de_pago:
    def __init__(self,ID_forma_de_pago,descripcion):
        self._ID_forma_de_pago = ID_forma_de_pago
        self._descripcion = descripcion
        
    @property
    def ID_forma_de_pago(self):
        return self._ID_forma_de_pago
    
    @property
    def descripcion(self):
        return self._descripcion
    
    @descripcion.setter
    def descripcion(self,nueva_descripcion):
        self._descripcion = nueva_descripcion
        
    
    def __str__(self):
        return f"ID_FORMA DE PAGO: {self.ID_forma_de_pago}, Descripcion: {self.descripcion}"