from Enums.Rol_enum import Rol
class Usuario:
    def __init__(self):
        
        self._pedidos = []
        
    @property
    def ID_usuario(self):
        return self._ID_usuario
    
    @ID_usuario.setter
    def ID_usuario(self,nombre_nuevo):
        self._ID_usuario = nombre_nuevo
    
    #decorador @property se usa cuando quieres realizar algún tipo de lógica de cálculo o validación al acceder al atributo
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self,nombre_nuevo):
        self._nombre = nombre_nuevo
    
    @property
    def apellido(self):
        return self._apellido
    
    @apellido.setter
    def apellido(self,apellido_nuevo):
        self._apellido = apellido_nuevo
    
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self,email_nuevo):
        self._email = email_nuevo
    
    
    @property
    def dni(self):
        return self._dni
    
    @dni.setter
    def dni(self,dni_nuevo):
        self._dni =dni_nuevo
    
    @property
    def domicilio(self):
        return self._domicilio
    
    @domicilio.setter
    def domicilio(self,domicilio_nuevo):
        self._domicilio = domicilio_nuevo
        
    
    def get_rol(self):
        return self._rol

    
    def set_rol(self, rol):
        if isinstance(rol, Rol):
            self._rol = rol
        else:
            raise ValueError("El valor de rol debe ser un objeto de la clase Rol")
    
   
    def get_pedidos(self):
        return self._pedidos
    
    
    #en el metodo str evito mostrar dni ya que por el momento lo usare de login para cada cliente en la consola  
    def __str__(self):
     return f"Usuario(ID: {self.ID_usuario}, Nombre: {self.nombre}, Apellido: {self.apellido}, Email: {self.email}, Domicilio: {self.domicilio}, Rol: {self.get_rol().value})"
    

    
