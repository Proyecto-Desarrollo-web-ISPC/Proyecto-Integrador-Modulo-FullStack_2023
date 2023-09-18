class Talle :
    def __init__(self):
        pass
    
    @property
    def ID_talle(self):
        return self._ID_talle
    
    @ID_talle.setter
    def ID_talle(self,nuevo_id):
        self._ID_talle = nuevo_id
    
    @property
    def talle(self):
        return self._talle
    
    @talle.setter
    def talle(self,nuevo_talle):
        self._talle = nuevo_talle
        
    def __str__(self):
        return (f"ID: {self.ID_talle}, TALLE: {self.talle}")