
class Producto:
    def __init__(self,ID_producto,nombre_producto,descripcion,talle,precio,stock):
        self._ID_producto = ID_producto
        self._nombre_producto = nombre_producto
        self._descripcion = descripcion
        self._talle = talle
        self._precio = precio
        self._stock = stock
        
    @property
    def ID_producto(self):
        return self._ID_producto
    
    @property
    def nombre_producto(self):
        return self._nombre_producto
    
    @nombre_producto.setter
    def nombre_producto(self,nombre):
        self._nombre_producto = nombre
        
    @property
    def descripcion(self):
        return self._descripcion
    
    @descripcion.setter
    def descripcion(self,nueva_descripcion):
        self._descripcion = nueva_descripcion
        
    @property
    def talle(self):
        return self._talle
    
    @talle.setter
    def talle(self,nuevo_talle):
        self._talle = nuevo_talle
        
    @property
    def precio(self):
        return self._precio
    
    @precio.setter
    def precio(self,nuevo_precio):
        self._precio = nuevo_precio
    
    @property
    def stock(self):
        return self._stock
    
    @stock.setter
    def stock(self,nuevo_stock):
        self._stock = nuevo_stock
        
    
    def mostrar_producto(self):
        return f"Producto(ID: {self.ID_producto}, Nombre del producto: {self.nombre_producto}, Descripcion: {self.descripcion}, Talle: {self.talle}, Precio: {self.precio}, Stock disponible: {self.stock})"
        
        
    