from Entidades.Usuario import *
from Repositorio.Usuario_repositorio import *
from Validaciones.validacion_campos import *
from tabulate import tabulate


def crear_usuario(num):
 try:
     
     usuario1= Usuario()
     while True:
      nombre= input("Por favor,ingrese su nombre: ")
      if validacion_campo(nombre) or validacion_caracter(nombre,"NOMBRE"):
       continue
      else:
         break
     usuario1.nombre= nombre
     while True:
      apellido=input("Ingrese su apellido: ")
      if validacion_campo(apellido) or validacion_caracter(apellido,"APELLIDO"):
          continue
      else:
          break
     usuario1.apellido= apellido
     while True:
      email=input("Ingrese su email: ")
      if validacion_campo(email):
          continue
      elif not validar_correo(email):
          print("debe ingresar un mail valido(@ y .)")
          continue
      else:
       mail=buscar_por_email(email)
       if mail is None:
        usuario1.email= email
        break
       else:
          print("el Email ya se encuentra registrado,intente nuevamente")
          continue
     try:
       while True:
        dni = int(input("Ingrese su numero de documento sin puntos: "))
        if validacion_numero(dni,"DNI"):
          continue
        else:
          break
     except:
         return print("El campo dni no puede estar vacio ni contener letras")
     user=buscar_usuario(dni)
     if user is None:
      usuario1.dni= dni
     else:
         return print("El DNI ya se encuentra registrado en nuestra base de datos,por favor intente nuevamente")
     
     domicilio=input("Ingrese su domicilio: ")
     validacion_campo(domicilio)
     usuario1.domicilio = domicilio
     
     if num == 1:
      usuario1.set_rol(Rol.CLIENTE)
     else:
      usuario1.set_rol(Rol.ADMIN)
     rol = usuario1.get_rol().value
     id= crear_user(usuario1)
     usuario1.ID_usuario=id
     return usuario1
     
             
 except ValueError as error:
  print("Error:", error)
  
  while True:
      email=input("Ingrese su email: ")
      if validacion_campo(email):
          continue
      elif not validar_correo(email):
          print("debe ingresar un mail valido(@ y .)")
          continue
      else:
       mail=buscar_por_email(email) 
  
  
  
def modificar_email(id):
 try:
    while True:
     Email=input("Ingrese el nuevo Email: ")
     if validacion_campo(Email):
        continue
     elif not validar_correo(Email):
          print("debe ingresar un mail valido(@ y .)")
          continue 
     else:
      mail=buscar_por_email(Email)
      if mail is None:
       nuevo_email =cambiar_mail(id,Email)
       print(f"El cambio de Email se registro correctamente.Su nuevo Email es {Email}")
       break
      else:
       print("el Email ya se encuentra registrado,intente nuevamente")
       continue
 except ValueError as error:
  print("Error:", error)

def modificar_domicilio(id):
 try:
    domicilio=input("Ingrese el nuevo Domicilio: ")
    validacion_campo(domicilio)
    nuevo_domicilio =cambiar_domicilio(id,domicilio)
    print(f"El cambio de Domicilio se registro correctamente.Su nuevo domicilio es {domicilio}")
 except ValueError as error:
  print("Error:", error)


#metodo a utilizar cuando ingreso como cliente   
def buscar_cliente():
    try:
     while True:
      dni=int(input("Por favor,ingrese el dni: "))
      if validacion_numero(dni,"DNI"):
          continue
      else:
          break
     cliente=buscar_usuario(dni)
     if cliente:
        encabezados = ["ID_Usuario", "Nombre", "Apellido", "Email", "Dni", "Domicilio", "ROL"]
        print(tabulate([cliente], headers=encabezados, tablefmt="pretty"))
        usuario1=Usuario()
        usuario1.ID_usuario= cliente[0]
        usuario1.nombre= cliente[1]
        usuario1.apellido= cliente[2]
        usuario1.email=cliente[3]
        usuario1.dni= cliente[4]
        usuario1.domicilio= cliente[5]
        usuario1._rol=cliente[6]
       
        return usuario1 # Retorna el cliente
     else:
        print("No se encontraron resultados,debe registrarse primero.")
       
    except ValueError as error:
     print("El campo dni no puede estar vacio,intente nuevamente mas tarde")
     
     
     
#servicios como administrador
def listar_clientes():
 clientes =buscar_todos()
 if clientes:
    encabezados = ["ID_Usuario", "Nombre", "Apellido", "Email", "Dni", "Domicilio", "ROL"]
    print(tabulate(clientes, headers=encabezados, tablefmt="pretty"))
 else:
    print("No se encontraron resultados.")
    
def buscar_usuario_por_id():
    try:
        id=int(input("Ingrese el id del usuario: "))
        user=buscar_por_id(id)
        if user:
         encabezados = ["ID_Usuario", "Nombre", "Apellido", "Email", "Dni", "Domicilio", "ROL"]
         print(tabulate([user], headers=encabezados, tablefmt="pretty"))
        else:
         print("No se encontraron resultados,debe registrarse primero.")
        
    except ValueError as error:
     print("El id debe ser un numero: no puede contener caracteres ni estar vacio")
     