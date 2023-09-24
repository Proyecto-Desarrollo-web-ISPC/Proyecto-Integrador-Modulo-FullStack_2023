
class Producto_talle:
    def __init__(self):
        pass
    
    
    @property
    def ID_producto_talle(self):
        return self._ID_producto_talle
    
    @ID_producto_talle.setter
    def ID_producto_talle(self,nuevo_id):
        self._ID_producto_talle=nuevo_id
        
    
    @property
    def ID_producto(self):
        return self._ID_producto
    
    @ID_producto.setter
    def ID_producto(self,idproducto_nuevo):
        self._ID_producto= idproducto_nuevo
    
    @property
    def ID_talle(self):
        return self._ID_talle
    
    @ID_talle.setter
    def ID_talle(self,idtalle_nuevo):
        self._ID_talle = idtalle_nuevo
    
    @property
    def stock(self):
        return self._stock
    
    @stock.setter
    def stock(self,nuevo_stock):
        self._stock = nuevo_stock
        
    def __str__(self):
        return (f"ID: {self.ID_producto_talle}, ID_producto {self.ID_producto}, ID_talle {self.ID_talle}, stock: {self.stock}")