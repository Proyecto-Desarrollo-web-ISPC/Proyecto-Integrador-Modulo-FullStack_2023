from Repositorio.Conexion import *

def crear_user(usuario):
     try:
        connection.connect()
        
        query = "INSERT INTO Usuarios(nombre,apellido,email,dni,domicilio,rol)VALUES (%s,%s,%s,%s,%s,%s)"
        connection.cursor.execute(query,(usuario.nombre,usuario.apellido,usuario.email,usuario.dni, usuario.domicilio,usuario.get_rol().value))
        connection.commit()
        id_insertado = connection.cursor.lastrowid
        print("El Usuario se inserto correctamente en la base de datos.")
        return id_insertado
        
     except mysql.connector.Error as err:
        print("Error al intentar insertar el Usuario:", err)
     finally:
         if connection:
            connection.close()
         

def buscar_usuario(dni):
   try:
        connection.connect()
        
        query = "SELECT * FROM Usuarios WHERE Dni = %s"
        value = (dni,)
        connection.cursor.execute(query, value)
        resultado = connection.cursor.fetchone()
        if resultado:
            return resultado
        else:
            return None
   except mysql.connector.Error as err:
        print("Error al buscar Usuario:", err)
   finally:
         if connection:
            connection.close()
            
            
def buscar_por_email(mail):
   try:
        connection.connect()
        
        query = "SELECT ID_usuario FROM Usuarios WHERE Email = %s"
        value = (mail,)
        connection.cursor.execute(query, value)
        resultado = connection.cursor.fetchone()
        if resultado:
            id = resultado[0]
            return id
        else:
            return None
   except mysql.connector.Error as err:
        print("Error,no se pudo buscar el mail:", err)
   finally:
         if connection:
            connection.close()

def buscar_por_id(id):
   try:
        connection.connect()
        
        query = "SELECT * FROM Usuarios WHERE id_usuario = %s"
        value = (id,)
        connection.cursor.execute(query, value)
        resultado = connection.cursor.fetchone()
        if resultado:
            return resultado
        else:
            return None
   except mysql.connector.Error as err:
        print("Error al buscar Usuario:", err)
   finally:
         if connection:
            connection.close()

            
def cambiar_mail(id_usuario,email_nuevo):
   try:
      connection.connect()
      query = "UPDATE usuarios SET email = %s WHERE ID_usuario = %s"
      value = (email_nuevo,id_usuario)
      connection.cursor.execute(query,value)
      connection.commit()
   
   except mysql.connector.Error as err:
        print("Error,no se pudo cambiar el Email,intente nuevamente:", err)
   finally:
         if connection:
            connection.close()  
            
  
def cambiar_domicilio(id_usuario,domicilio_nuevo):
   try:
      connection.connect()
      query = "UPDATE usuarios SET domicilio = %s WHERE ID_usuario = %s"
      value = (domicilio_nuevo,id_usuario)
      connection.cursor.execute(query,value)
      connection.commit()
   
   except mysql.connector.Error as err:
        print("Error,no se pudo cambiar el domicilio,intente nuevamente:", err)
   finally:
         if connection:
            connection.close()  
  
  
  
  
  
  
  
  
  
  
 #repo de admin           
def buscar_todos():
    try:
        connection.connect()
        query = "SELECT * FROM Usuarios WHERE Rol = %s"
        value = (1,)
        connection.cursor.execute(query,value)
        resultados =connection.cursor.fetchall()
        return resultados

    except mysql.connector.Error as err:
        print("Error al buscar Usuarios:", err)
    finally: 
        connection.close()
        
        
