class Detalle_pedido :
    def __init__(self,ID_detalle,ID_pedido,ID_producto,cantidad,subtotal):
        self._ID_detalle = ID_detalle
        self._ID_pedido = ID_pedido
        self._ID_producto = ID_producto
        self._cantidad = cantidad
        self._subtotal = subtotal
        
    @property
    def ID_detalle(self):
        return self._ID_detalle
    
    @property
    def ID_pedido(self):
        return self._ID_pedido
    
    @property
    def ID_producto(self):
        return self._ID_producto
    
    @property
    def cantidad(self):
        return self._cantidad
    
    @cantidad.setter
    def cantidad(self,nueva_cantidad):
        self._cantidad = nueva_cantidad
        
    @property
    def subtotal(self):
        return self._subtotal
    
    @cantidad.setter
    def cantidad(self,nueva_cantidad):
        self._cantidad = nueva_cantidad
        
    def __str__(self):
        return f"DETALLE DEL PEDIDO : ID: {self.ID_detalle},ID DEL PEDIDO: {self.ID_pedido}, ID DEL PRODUCTO: {self.ID_producto}, Cantidad comprada: {self.cantidad}, Subtotal: {self.subtotal}"