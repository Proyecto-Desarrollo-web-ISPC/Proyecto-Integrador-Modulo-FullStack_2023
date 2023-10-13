from datetime import *
from Repositorio.Conexion import *


def insertar_pedido(pedido):
     try:
        connection.connect()
        
        query = "INSERT INTO Pedidos(fecha,ID_usuario,Total,Estado)VALUES (%s,%s,%s,%s)"
        connection.cursor.execute(query,(pedido.fecha,pedido.ID_usuario,pedido.total,pedido.get_estado().value))
        connection.commit()
        id_insertado = connection.cursor.lastrowid
        return id_insertado
        
     except mysql.connector.Error as err:
        print("Error al insertar el pedido:", err)
     finally:
         if connection:
            connection.close()
            

def buscar_pedido(id):
 try:
     connection.connect()
        
     query = "SELECT * FROM pedidos WHERE ID_PEDIDO = %s"
     value = (id,)
     connection.cursor.execute(query, value)
     pedido = connection.cursor.fetchone()
     if pedido is not None:
      return pedido
     else:
         return None
        
 except mysql.connector.Error as err:
        print("Error,no se encontro el pedido:", err)
 finally:
         if connection:
            connection.close()






            
def modificar_total(total,id):
    try:
        connection.connect()
        query="UPDATE Pedidos SET Total =(%s) WHERE ID_pedido = (%s)"
        values=(total,id)
        connection.cursor.execute(query, values)
        connection.commit()
        print("se actualizo el total del pedido")
        
    except mysql.connector.Error as err:
        print("Error al modificar el total:", err)
    finally:
         if connection:
            connection.close()
            
            
          
def modificar_estado(estado,id):
    try:
        connection.connect()
        query="UPDATE Pedidos SET Estado =(%s) WHERE ID_pedido = (%s)"
        values=(estado,id)
        connection.cursor.execute(query, values)
        connection.commit()
        if connection.cursor.rowcount > 0:
            print("El estado del pedido fue modificado")
            return True
        else:
            print("El pedido ya estaba en el estado deseado")
            return False
        
    except mysql.connector.Error as err:
        print("Error al modificar el estado del pedido:", err)
    finally:
         if connection:
            connection.close()
            
            
def listar_pedidos(id):
    try:
        connection.connect()
        query = """
        SELECT
        P.id_pedido,
        DP.subtotal,
        DP.cantidad,
        DP.id_talle,
        T.talle AS talle,
        DP.id_producto,
        PR.nombre_producto AS nombre_producto,
        P.fecha,
        P.total
        FROM Pedidos P
        INNER JOIN Detalles_Pedido DP ON P.id_pedido = DP.id_pedido
        INNER JOIN Productos PR ON DP.id_producto = PR.id_producto
        INNER JOIN Talles T ON DP.id_talle = T.id_talle
        WHERE ID_usuario = %s
        AND Estado = 'aceptado'
        ORDER BY P.id_pedido;""" 
        value = (id,)
        connection.cursor.execute(query, value)
        resultado = connection.cursor.fetchall()
        if resultado:
            return resultado
        else:
            return None
    except mysql.connector.Error as err:
        print("Error al Buscar pedidos:", err)
    finally:
         if connection:
            connection.close()
            


def listar_ventas():
    try:
        connection.connect()
        query = """
        SELECT
        p.id_usuario,
        P.id_pedido,
        DP.subtotal,
        DP.cantidad,
        DP.id_talle,
        T.talle AS talle,
        DP.id_producto,
        PR.nombre_producto AS nombre_producto,
        P.fecha,
        P.total
        FROM Pedidos P
        INNER JOIN Detalles_Pedido DP ON P.id_pedido = DP.id_pedido
        INNER JOIN Productos PR ON DP.id_producto = PR.id_producto
        INNER JOIN Talles T ON DP.id_talle = T.id_talle
        WHERE Estado = 'aceptado'
        ORDER BY P.id_pedido;
        """ 
        connection.cursor.execute(query)
        resultado = connection.cursor.fetchall()
        if resultado:
            return resultado
        else:
            return None
    except mysql.connector.Error as err:
        print("Error al Buscar pedidos:", err)
    finally:
         if connection:
            connection.close()


def calcular_total_ventas():
    try:
        connection.connect()
        query = """
        SELECT
        SUM(P.total) AS total_ventas
        FROM Pedidos P
        WHERE P.Estado = 'aceptado'
        """
        connection.cursor.execute(query)
        resultado = connection.cursor.fetchone()
        if resultado:
            total_ventas = resultado[0]
            return total_ventas
        else:
            return None
    except mysql.connector.Error as err:
        print("Error al calcular el total de ventas:", err)
    finally:
        if connection:
            connection.close()



 
 #services detalle_pedido
            
def insertar_detalle(detalle):
     try:
        connection.connect()
        
        query = "INSERT INTO detalles_pedido(ID_pedido,ID_producto,ID_talle,cantidad,subtotal)VALUES (%s,%s,%s,%s,%s)"
        connection.cursor.execute(query,(detalle.ID_pedido,detalle.ID_producto,detalle.ID_talle,detalle.cantidad,detalle.subtotal))
        connection.commit()
        id_insertado = connection.cursor.lastrowid
        return id_insertado
        
     except mysql.connector.Error as err:
        print("EL detalle no pudo ser insertado:", err)
     finally:
         if connection:
            connection.close()
            
def buscar_detalle(id):
    try:
        connection.connect()
        
        query = "SELECT * FROM detalles_pedido WHERE ID_PEDIDO = %s"
        value = (id,)
        connection.cursor.execute(query, value)
        detalle = connection.cursor.fetchall()
        return detalle
        
    except mysql.connector.Error as err:
        print("Error al buscar el detalle:", err)
    finally:
         if connection:
            connection.close()
            
            
            

def eliminar_detalles_pedido(id):
    try:
        connection.connect()
        query="DELETE from detalles_pedido WHERE ID_pedido = %s"
        value=(id,)
        connection.cursor.execute(query,value)
        connection.commit()
    except mysql.connector.Error as err:
        print("error al borrar el pedido:", err)
    finally:
         if connection:
            connection.close()    
            
            
            
#formas de pago
def formas_de_pago():
    try:
        connection.connect()
        query="SELECT descripcion from formas_de_pago"
        connection.cursor.execute(query)
        formas = connection.cursor.fetchall()
        return formas
    except mysql.connector.Error as err:
        print("ocurrio un error:", err)
    finally:
         if connection:
            connection.close()  
            
            
def buscar_forma_pago(descripcion):
    try:
     connection.connect()
        
     query = "SELECT ID_forma_de_pago from formas_de_pago WHERE Descripcion = %s"
     value = (descripcion,)
     connection.cursor.execute(query, value)
     resultado = connection.cursor.fetchone()
     if resultado:
      id = resultado[0]
      return id
     else:
      return None
        
    except mysql.connector.Error as err:
        print("Lo sentimos,no aceptamos esa forma de pago aun:", err)
    finally:
         if connection:
            connection.close()
            
def listar_tarjetas():
    try:
     connection.connect()  
     query = "SELECT * FROM tarjetas "
     connection.cursor.execute(query)
     resultados= connection.cursor.fetchall()
     return resultados 
    except mysql.connector.Error as err:
        print("Lo sentimos,ocurrio un error:", err)
    finally:
         if connection:
            connection.close()
            
            
def buscar_tarjeta(nombre):
    try:
     connection.connect()  
     query = "SELECT * FROM tarjetas where Nombre_tarjeta = %s "
     value = (nombre,)
     connection.cursor.execute(query, value)
     tarjeta = connection.cursor.fetchone()
     if tarjeta:
         return tarjeta
     else:
         return None
        
    except mysql.connector.Error as err:
        print("Lo sentimos,ocurrio un error:", err)
    finally:
         if connection:
            connection.close()
            
            
def insertar_pago_pedido(id_pedido,id_forma_depago,id_tarjeta):
    try:
        connection.connect()
        query = "INSERT INTO formas_depago_pedidos(ID_pedido,ID_forma_de_pago,ID_tarjeta)VALUES (%s,%s,%s)"
        values=(id_pedido,id_forma_depago,id_tarjeta)
        connection.cursor.execute(query,values)
        connection.commit()
        id = connection.cursor.lastrowid
        if id:
            return id
        else:
            return None
        
    except mysql.connector.Error as err:
        print("Error al insertar forma de pago:", err)
    finally:
         if connection:
            connection.close()
  
#lista de pedidos para que el administrador lleve un control de ventas          
def listar_ventas_detalladas(mes):
    try:
        connection.connect()
        query = """
        SELECT
        P.id_usuario,
        P.id_pedido,
        DP.subtotal,
        DP.cantidad,
        DP.id_talle,
        T.talle AS talle,
        DP.id_producto,
        PR.nombre_producto AS nombre_producto,
        P.fecha,
        P.total
        FROM Pedidos P
        INNER JOIN Detalles_Pedido DP ON P.id_pedido = DP.id_pedido
        INNER JOIN Productos PR ON DP.id_producto = PR.id_producto
        INNER JOIN Talles T ON DP.id_talle = T.id_talle
        WHERE P.Estado = 'aceptado'
        AND DATE_FORMAT(P.fecha, '%Y-%m') = %s
        ORDER BY P.id_pedido;
        """
        value= (mes,)
        connection.cursor.execute(query,value)
        resultado = connection.cursor.fetchall()
        if resultado:
            return resultado
        else:
            return None
    except mysql.connector.Error as err:
        print("Error al buscar ventas:", err)
    finally:
        if connection:
            connection.close()
            
def listar_ventas_por_mes(mes):
    try:
        connection.connect()
        query = """
        SELECT
        P.id_usuario,
        P.id_pedido,
        P.fecha,
        P.total
        FROM Pedidos P
        WHERE P.Estado = 'aceptado'
        AND DATE_FORMAT(P.fecha, '%Y-%m') = %s
        ORDER BY P.id_pedido;
        """
        value= (mes,)
        connection.cursor.execute(query,value)
        resultado = connection.cursor.fetchall()
        if resultado:
            return resultado
        else:
            return None
    except mysql.connector.Error as err:
        print("Error al buscar ventas:", err)
    finally:
        if connection:
            connection.close()           
            

            
def calcular_total_mensual(mes):
    try:
        connection.connect()
        query = """
        SELECT
        SUM(P.total) AS total_ventas
        FROM Pedidos P
        WHERE P.Estado = 'aceptado'
        AND DATE_FORMAT(P.fecha, '%Y-%m') = %s
        """
        value= (mes,)
        connection.cursor.execute(query,value)
        resultado = connection.cursor.fetchone()
        if resultado:
            total_ventas = resultado[0]
            return total_ventas
        else:
            return None
    except mysql.connector.Error as err:
        print("Error al calcular el total de ventas:", err)
    finally:
        if connection:
            connection.close()
            
            
            
def calcular_mensual_segun_forma_de_pago(mes,forma_de_pago):
    try:
        connection.connect()
        query = """
        SELECT
        P.id_pedido,
        F.descripcion AS forma_de_pago,
        P.total,
        DATE_FORMAT(P.fecha, '%Y-%m') AS mes,
        SUM(P.total) OVER (PARTITION BY DATE_FORMAT(P.fecha, '%Y-%m'), F.descripcion) AS venta_mensual
        FROM Pedidos P
        JOIN formas_depago_pedidos FP ON P.id_pedido = FP.id_pedido
        JOIN formas_de_pago F ON FP.id_forma_de_pago = F.id_forma_de_pago
        WHERE F.descripcion = %s
        AND P.estado = 'aceptado'
        AND DATE_FORMAT(P.fecha, '%Y-%m') = %s
        """
        values=(forma_de_pago,mes)
        connection.cursor.execute(query,values)
        resultado = connection.cursor.fetchall()
        if resultado:
            return resultado
        else:
            return None
    except mysql.connector.Error as err:
        print("Error al obtener los pedidos:", err)
    finally:
        if connection:
            connection.close()
            
def calcular_total_mensual_por_metodo_de_pago(mes,metodo_de_pago):
    try:
        connection.connect()
        query = """
        SELECT
        SUM(P.total) AS total_ventas
        FROM Pedidos P
        JOIN formas_depago_pedidos FP ON P.id_pedido = FP.id_pedido
        JOIN formas_de_pago F ON FP.id_forma_de_pago = F.id_forma_de_pago
        WHERE P.Estado = 'aceptado'
        AND DATE_FORMAT(P.fecha, '%Y-%m') = %s
        AND F.descripcion = %s
        """
        values = (mes,metodo_de_pago)
        connection.cursor.execute(query, values)
        resultado = connection.cursor.fetchone()
        if resultado:
            total_ventas = resultado[0]
            return total_ventas
        else:
            return None
    except mysql.connector.Error as err:
        print("Error al calcular el total de ventas:", err)
    finally:
        if connection:
            connection.close()
            
            
def calcular_total_anual(year):
    try:
        connection.connect()
        query = """
        SELECT
        SUM(P.total) AS total_ventas
        FROM Pedidos P
        WHERE P.Estado = 'aceptado'
        AND YEAR(P.fecha) = %s
        """
        value = (year,)
        connection.cursor.execute(query, value)
        resultado = connection.cursor.fetchone()
        if resultado:
            total_ventas = resultado[0]
            return total_ventas
        else:
            return None
    except mysql.connector.Error as err:
        print("Error al calcular el total de ventas:", err)
    finally:
        if connection:
            connection.close()
            
def listar_ventas_por_year(year):
    try:
        connection.connect()
        query = """
        SELECT
        P.id_usuario,
        P.id_pedido,
        P.fecha,
        P.total
        FROM Pedidos P
        WHERE P.Estado = 'aceptado'
        AND YEAR(P.fecha) = %s
        ORDER BY P.id_pedido;
        """
        value = (year,)
        connection.cursor.execute(query, value)
        resultado = connection.cursor.fetchall()
        if resultado:
            return resultado
        else:
            return None
    except mysql.connector.Error as err:
        print("Error al buscar ventas:", err)
    finally:
        if connection:
            connection.close()
            
            
def ver_pedidos_cancelados(mes):
    try:
        connection.connect()
        query = """
        SELECT *
        FROM Pedidos P
        WHERE P.Estado = 'cancelado'
        AND DATE_FORMAT(P.fecha, '%Y-%m') = %s
        ORDER BY P.id_pedido;
        """
        value= (mes,)
        connection.cursor.execute(query,value)
        resultado = connection.cursor.fetchall()
        if resultado:
            return resultado
        else:
            return None
    except mysql.connector.Error as err:
        print("Error al buscar ventas:", err)
    finally:
        if connection:
            connection.close()