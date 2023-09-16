
class Pedido:
    def __init__(self, ID_pedido, fecha, ID_usuario, total, Estado):
        self._ID_pedido = ID_pedido
        self._fecha = fecha
        self._ID_usuario = ID_usuario
        self._total = total
        self._Estado = Estado
        self._formas_de_pago = [] 
        
    @property
    def ID_pedido(self):
        return self._ID_pedido
         
    @property
    def fecha(self):
        return self._fecha
    
    @fecha.setter
    def fecha(self,fecha_nueva):
        self._fecha = fecha_nueva
      
    #de id_usuario solo establezco el getter y no el setter ya que es una clave foranea y no voy a necesitar setearlo 
    @property
    def ID_usuario(self):
        return self._ID_usuario
    
    @property
    def total(self):
        return self._total
    
    @total.setter
    def total(self,total_nuevo):
        self._total = total_nuevo
        
    @property
    def Estado(self):
        return self._Estado
    
    @Estado.setter
    def Estado(self,Estado_nuevo):
        self._Estado = Estado_nuevo
        
    
        
    
    def __str__(self):
        return f"PEDIDO(ID:{self.ID_pedido}, Fecha: {self.fecha}, ID_usuario: {self.ID_usuario}, Total: {self.total}, Estado: {self.Estado.value})"
    
    
