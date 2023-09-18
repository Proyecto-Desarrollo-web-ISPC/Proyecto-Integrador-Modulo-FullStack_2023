from Entidades.Usuario import *
from Repositorio.Usuario_repositorio import *
from Validaciones.validacion_campos import *
from tabulate import tabulate


def crear_usuario(num):
 try:
     
     usuario1= Usuario()
     nombre= input("Por favor,ingrese su nombre: ")
     validacion_campo(nombre) or validacion_caracter(nombre,"NOMBRE")
     usuario1.nombre= nombre
     
     apellido=input("Ingrese su apellido: ")
     validacion_campo(apellido) or validacion_caracter(apellido,"APELLIDO")
     usuario1.apellido= apellido
     
     email=input("Ingrese su email: ")
     validacion_campo(email)
     mail=buscar_por_email(email)
     if mail is None:
      usuario1.email= email
     else:
         return print("el Email ya se encuentra registrado,intente nuevamente")
     
     dni = int(input("Ingrese su numero de documento sin puntos: "))
     validacion_numero(dni,"DNI")
     user=buscar_usuario(dni)
     if user is None:
      usuario1.dni= dni
     else:
         return print("El Usuario ya existe en nuestra base de datos, intente nuevamente")
     
     domicilio=input("Ingrese su domicilio: ")
     validacion_campo(domicilio)
     usuario1.domicilio = domicilio
     
     if num == 1:
      usuario1.set_rol(Rol.CLIENTE)
     else:
      usuario1.set_rol(Rol.ADMIN)
     rol = usuario1.get_rol().value
     id= crear_user(nombre,apellido,email,dni,domicilio,rol)
     usuario1.ID_usuario=id
     return usuario1
     
             
 except ValueError as error:
  print("Error:", error)
  
  
def modificar_email(id):
 try:
    Email=input("Ingrese el nuevo Email: ")
    validacion_campo(Email)
    nuevo_email =cambiar_mail(id,Email)
    print(f"El cambio de Email se registro correctamente.Su nuevo Email es {Email}")
 except ValueError as error:
  print("Error:", error)


#servicios como administrador
def listar_clientes():
 clientes =buscar_todos()
 if clientes:
    encabezados = ["ID_Usuario", "Nombre", "Apellido", "Email", "Dni", "Domicilio", "ROL"]
    print(tabulate(clientes, headers=encabezados, tablefmt="pretty"))
 else:
    print("No se encontraron resultados.")
    
  
#metodo a utilizar cuando ingreso como cliente   
def buscar_cliente():
    try:
     dni=int(input("Por favor,ingrese su dni: "))
     validacion_numero(dni,"DNI")
     cliente=buscar_usuario(dni)
     if cliente:
        encabezados = ["ID_Usuario", "Nombre", "Apellido", "Email", "Dni", "Domicilio", "ROL"]
        print(tabulate([cliente], headers=encabezados, tablefmt="pretty"))
        id_usuario = cliente[0]  # Obtiene el valor del ID de usuario desde la variable cliente
        return id_usuario  # Retorna el ID de usuario
     else:
        print("No se encontraron resultados.")
       
    
    except ValueError as error:
     print("Error:", error)