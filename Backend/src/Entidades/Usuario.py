from Enums import Rol_enum
class Usuario:
    def __init__(self,ID_usuario,nombre,apellido,email,dni,domicilio,Rol):
        self._ID_usuario = ID_usuario
        self._nombre = nombre
        self._apellido = apellido
        self._email = email
        self._dni = dni
        self._domicilio = domicilio
        self._Rol = Rol
        self._pedidos = []
        
    @property
    def ID_usuario(self):
        return self._ID_usuario
    
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
        self._Email = email_nuevo
    
    
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
        
    @property
    def Rol(self):
        return self._Rol
    
    @Rol.setter
    def Rol(self,Rol_nuevo):
        self._Rol = Rol_nuevo
    
    #en este caso no  hace falta usar el decorador ya que es una lista vacia y actua como un atributo de instancia normal
    #pero lo dejo a modo guia para mis compañeros   
    @property
    def get_pedidos(self):
        return self._pedidos
    
    
    #en el metodo str evito mostrar dni ya que por el momento lo usare de login para cada cliente en la consola  
    def __str__(self):
     return f"Usuario(ID: {self.ID_usuario}, Nombre: {self.nombre}, Apellido: {self.apellido}, Email: {self.email}, Domicilio: {self.domicilio}, Rol: {self.Rol})"
    

    
