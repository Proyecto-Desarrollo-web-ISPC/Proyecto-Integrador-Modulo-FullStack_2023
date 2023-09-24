class Detalle_pedido :
    
    def __init__(self) :
        pass
        
         
       
        
    @property
    def ID_detalle(self):
        return self._ID_detalle
    @ID_detalle.setter
    def ID_detalle(self,nuevo_id):
        self._ID_detalle =nuevo_id
    
    @property
    def ID_pedido(self):
        return self._ID_pedido
    
    @ID_pedido.setter
    def ID_pedido(self,pedidoid_nuevo):
        self._ID_pedido = pedidoid_nuevo
    
    @property
    def ID_producto(self):
        return self._ID_producto
    
    @ID_producto.setter
    def ID_producto(self,product_id):
        self._ID_producto= product_id
    
    @property
    def cantidad(self):
        return self._cantidad
    
    @cantidad.setter
    def cantidad(self,nueva_cantidad):
        self._cantidad = nueva_cantidad
        
    @property
    def subtotal(self):
        return self._subtotal
    
    @subtotal.setter
    def subtotal(self,nuevo_subtotal):
        self._subtotal = nuevo_subtotal
        
    def __str__(self):
        return f"DETALLE DEL PEDIDO : ID: {self.ID_detalle},ID DEL PEDIDO: {self.ID_pedido}, ID DEL PRODUCTO: {self.ID_producto}, Cantidad comprada: {self.cantidad}, Subtotal: {self.subtotal}"