from Repositorio.Conexion import *

def crear_product(producto):
     try:
        connection.connect()
        
        query = "INSERT INTO Productos(nombre_producto,descripcion,precio)VALUES (%s,%s,%s)"
        connection.cursor.execute(query, (producto.nombre_producto,producto.descripcion,producto.precio))
        connection.commit()
        id_insertado = connection.cursor.lastrowid
        return id_insertado
        
     except mysql.connector.Error as err:
        print("Error al crear el producto:", err)
     finally:
         if connection:
            connection.close()
         
         
         
         
def buscar_id_talle(talle):
    try:
        connection.connect()
        
        query = "SELECT ID_talle FROM talles WHERE talle = %s"
        value = (talle,)
        connection.cursor.execute(query, value)
        resultado = connection.cursor.fetchone()
        if resultado:
            id_talle = resultado[0]
            return id_talle
        else:
            return None
    except mysql.connector.Error as err:
        print("Error al buscar el talle:", err)
    finally:
         if connection:
            connection.close()
            
            
def insert_producto_talle(producto_talle):
    try:
        connection.connect()
        
        query = "INSERT INTO Productos_talles(ID_producto,ID_talle,Stock)VALUES (%s,%s,%s)"
        connection.cursor.execute(query, (producto_talle.ID_producto,producto_talle.ID_talle,producto_talle.stock))
        connection.commit()
        id_insertado = connection.cursor.lastrowid
        return id_insertado
        
    except mysql.connector.Error as err:
        print("Error al cargar el producto:", err)
    finally:
         if connection:
            connection.close()
            

def buscar_producto(nombre):
    try:
        connection.connect()
        
        query = "SELECT * FROM Productos WHERE RTRIM(Nombre_producto) LIKE %s "
        value = (nombre,)
        connection.cursor.execute(query, value)
        resultado = connection.cursor.fetchone()
        if resultado:  
            return resultado
        else:
            return None
    except mysql.connector.Error as err:
        print("Error al Buscar el producto:", err)
    finally:
         if connection:
            connection.close()
            
            
#metodo a utilizar cuando haga un pedido       
def modify_stock(producto_talle):
    try:
        connection.connect()
        
        query = "UPDATE productos_talles SET stock = %s WHERE ID_producto = %s AND ID_talle = %s"
        connection.cursor.execute(query,(producto_talle.stock,producto_talle.ID_producto,producto_talle.ID_talle))
        connection.commit()
    except mysql.connector.Error as err:
        print("Error al modificar el stock:", err)
    finally:
         if connection:
            connection.close()
            

def modify_nombre_producto(nombre_nuevo,id_producto):
    try:
        connection.connect()
        
        query = "UPDATE Productos SET Nombre_producto = %s WHERE ID_producto = %s"
        value = (nombre_nuevo,id_producto)
        connection.cursor.execute(query, value)
        connection.commit()
        print(f"El nombre del producto fue modificado existosamente a {nombre_nuevo}")
    except mysql.connector.Error as err:
        print("Error al modificar el nombre:", err)
    finally:
         if connection:
            connection.close()
            
            
def all_products(nombre):
     try:
        connection.connect()
        query = """SELECT
        p.nombre_producto,
        p.precio,
        t.talle,
        pt.stock
        FROM productos p 
        INNER JOIN productos_talles pt ON p.id_producto = pt.id_producto
        INNER JOIN talles t ON pt.id_talle = t.id_talle 
        WHERE pt.stock > 0 AND p.nombre_producto LIKE %s 
        ORDER BY ID_producto_talle;"""
        value = (('%' + nombre + '%',))
        connection.cursor.execute(query,value)
        resultado = connection.cursor.fetchall()
        if resultado:
            return resultado
        else:
            return None
     except mysql.connector.Error as err:
        print("Error al Buscar el producto:", err)
     finally:
         if connection:
            connection.close()
            


def buscar_id_producto_talle(id_talle,producto_id):
     try:
        connection.connect()
        
        query = "SELECT * FROM productos_talles WHERE ID_talle = %s and ID_producto= %s"
        value = (id_talle,producto_id)
        connection.cursor.execute(query, value)
        resultado = connection.cursor.fetchone()
        if resultado:
            return resultado
        else:
            return None
     except mysql.connector.Error as err:
        print("Error al Buscar el producto:", err)
     finally:
         if connection:
            connection.close()
            
            
def consultar_stock(id_producto,id_talle):
    try:
        connection.connect()
        
        query = "SELECT stock FROM productos_talles WHERE ID_producto = %s AND ID_talle = %s"
        values = (id_producto,id_talle)
        connection.cursor.execute(query, values)
        resultado = connection.cursor.fetchone()
        if resultado:
            return resultado[0]
        else:
            return None  
    except mysql.connector.Error as err:
        print("Error al consultar el stock:", err)
    finally:
         if connection:
            connection.close()
            
            
            
def modify_precio(precio_nuevo,id_producto):
    try:
        connection.connect()
        
        query = "UPDATE Productos SET precio = %s WHERE ID_producto = %s"
        value = (precio_nuevo,id_producto)
        connection.cursor.execute(query, value)
        connection.commit()
        print(f"El precio del producto fue modificado existosamente a ${precio_nuevo}")
    except mysql.connector.Error as err:
        print("Error al modificar el precio:", err)
    finally:
         if connection:
            connection.close()
            
            
def listarProductos():
     try:
        connection.connect()
        query = """SELECT DISTINCT p.Nombre_producto, p.precio
        FROM productos p
        INNER JOIN productos_talles pt ON p.id_producto = pt.id_producto
        WHERE pt.stock > 0"""
        connection.cursor.execute(query)
        resultados = connection.cursor.fetchall()
        return resultados
       
     except mysql.connector.Error as err:
        print("Error al Buscar el producto:", err)
     finally:
         if connection:
            connection.close()
            
            
            
def listar_descripcion():
    try:
        connection.connect()
        query = "SELECT Nombre_producto,descripcion FROM productos"
        connection.cursor.execute(query)
        resultados = connection.cursor.fetchall()
        return resultados
       
    except mysql.connector.Error as err:
        print("Error al listar el producto:", err)
    finally:
         if connection:
            connection.close()
            
            
def cambiar_descripcion(descripcion,id_producto):
    try:
        connection.connect()
        
        query = "UPDATE Productos SET descripcion = %s WHERE ID_producto = %s"
        value = (descripcion,id_producto)
        connection.cursor.execute(query, value)
        connection.commit()
        print(f"La descripcion del producto fue modificado existosamente")
    except mysql.connector.Error as err:
        print("Error al modificar la descripcion:", err)
    finally:
         if connection:
            connection.close()
            
            
def listar_talles():
     try:
        connection.connect()
        query = "SELECT talle FROM talles"
        connection.cursor.execute(query)
        resultados = connection.cursor.fetchall()
        return resultados
       
     except mysql.connector.Error as err:
        print("Error al Buscar el producto:", err)
     finally:
         if connection:
            connection.close()