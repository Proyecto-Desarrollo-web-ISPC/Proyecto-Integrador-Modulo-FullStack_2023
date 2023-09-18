
class Producto:
    def __init__(self):
        pass
        
    @property
    def ID_producto(self):
        return self._ID_producto
    
    @ID_producto.setter
    def ID_producto(self,nuevo_id):
        self._ID_producto = nuevo_id
    
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
    def precio(self):
        return self._precio
    
    @precio.setter
    def precio(self,nuevo_precio):
        self._precio = nuevo_precio
    
    
    def mostrar_producto(self):
        return f"Producto(ID: {self.ID_producto}, Nombre del producto: {self.nombre_producto}, Descripcion: {self.descripcion}, Precio: {self.precio})"
        
        
    