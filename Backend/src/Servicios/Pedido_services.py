import datetime
from Entidades.Pedido import *
from Entidades.Detalle_pedido import *
from Entidades.Forma_de_pago import *
from Validaciones.validacion_campos import *
from Repositorio.Pedido_repositorio import *
from Repositorio.Producto_repositorio import *
from Servicios.Producto_services import *
from tabulate import tabulate
from datetime import *

def crear_pedido(id):
 try:
    #instancio un objeto pedido y lo seteo
    
    pedido1=Pedido()
    fecha_actual = date.today()
    pedido1.fecha = fecha_actual
    pedido1.ID_usuario= id
    pedido1.set_estado(Estado.ACEPTADO)
    #creo el detalle del pedido y lo guardo en una lista
    listas=crear_detalle()
    if not listas :
        return print("ocurrio un error,vuelva a intentarlo nuevamente")
    else:
     total_pedido =sum(subtotal for (_, _,_,subtotal) in listas)
    pedido1.total= total_pedido
    #persisto el pedido en la base de datos para tomar el id
    id_pedido=insertar_pedido(pedido1)
    if id_pedido is None:
        print("no se pudo insertar el pedido")
        return
    pedido1.ID_pedido=id_pedido
    #recorro la lista recibida de la funcion crear detalle para persistirla y asociarla al pedido previamente creado
    for lista  in listas:
     detalle=Detalle_pedido()
     detalle.ID_pedido= pedido1.ID_pedido
     detalle.ID_producto=lista[0]
     detalle.ID_talle= lista[1]
     detalle.cantidad= lista[2]
     detalle.subtotal= lista[3]
     insertar_detalle(detalle)
    #selecciono la forma de pago
    print(f"el total del pedido es {total_pedido},¿como desea abonar?")
    print("estas son nuestras formas de pago disponibles.¡EL PAGO CON TARJETA DE CREDITO TIENE UN RECARGO DEL 20%!:")
    metodos=formas_de_pago()
    while True:
        if metodos:
         encabezados = ["Metodo de pago"]
         print(tabulate(metodos, headers=encabezados, tablefmt="pretty"))
        metodo_de_pago=input("ingrese el metodo de pago que desea utilizar: ")
        if validacion_campo(metodo_de_pago):
          continue
        id_metodo=buscar_forma_pago(metodo_de_pago)
        if id_metodo is None:
             print("Lo sentimos,no disponemos de esa forma de pago.intente nuevamente con otra forma de pago")
             continue
        elif metodo_de_pago.lower() == "tarjeta de credito".lower():
         print("Estas son las tarjetas de credito que aceptamos.todas tienen un 20% de recargo")
         tarjetas_aceptadas=listar_tarjetas()
         encabezados = ["ID_tarjeta", "Nombre Tarjeta"]
         print(tabulate(tarjetas_aceptadas, headers=encabezados, tablefmt="pretty"))
         nombre_tarjeta=input("Ingrese el nombre de la tarjeta con la que desea pagar: ")
         if validacion_campo(nombre_tarjeta):
          continue
         tarjeta= buscar_tarjeta(nombre_tarjeta)
         if tarjeta is None:
          print("Lo sentimos,no trabajamos esa tarjeta de credito")
          continue
         insertar_pago= insertar_pago_pedido(id_pedido,id_metodo,tarjeta[0])
         if insertar_pago is None:
          print("ocurrio un error")
          continue
         else:
             nuevo_total= total_pedido + (total_pedido * 0.2)
             modificar_total(nuevo_total,id_pedido)
             print(f"El monto total de su pedido es {nuevo_total}.Muchas gracias por su compra")
             break
        else:
            insertar_pago= insertar_pago_pedido(id_pedido,id_metodo,None)
            print(f"Eligio {metodo_de_pago} como metodo de pago. El monto del pedido es {total_pedido},muchas gracias por comprar en nuestra tienda.")
            break   
 except ValueError as error:
     estado = "cancelado"
     modificar_estado(estado,id_pedido)
     cancelar_detalle(listas)
     eliminar_detalles_pedido(id_pedido)
     print("Error:", error)
            
    
     
     

def crear_detalle():
 try:
     Lista_detalles = []
     while True:
        print("ESTA ES NUESTRA LISTA DE PRODUCTOS")
        listar_todos_productos()
        while True:
         producto_name=input("Por favor,ingresa el nombre del producto que desea comprar (ingresa el año del mundial,pais,y si es titular o suplente): ")
         if validacion_campo(producto_name):
           continue
         else:
              break
        producto=buscar_producto(producto_name)  
        if producto is None:
         print("Lo sentimos,el producto no existe en nuestra base de datos")
         continue 
        #muestro los productos segun el stock
        listado=all_products(producto_name)
        if listado:
         encabezados = [ "Nombre producto", "Precio", "Talle","Stock disponible"]
         print(tabulate(listado, headers=encabezados, tablefmt="pretty"))
        else:
         print("No se encontro ese producto en nuestra base de datos,lo sentimos.")
         continue
        while True:
         talle=input("Ingrese el talle de la camiseta que desea comprar: ") 
         if validacion_campo(talle):
           continue 
         else:
              break
        #busco id del talle
        id_talle= buscar_id_talle(talle)
        if id_talle is None:
         print("No se encontro ese talle en nuestra base de datos")
         continue
        try:
         while True:
          cantidad=int(input("ingrese la cantidad de camisetas de ese talle que desea comprar: "))
          if validacion_numero(cantidad,"Cantidad"):
             continue
          else:
             break
        except:
             raise ValueError("La cantidad de camisetas no debe ser un caracter o estar vacia")   
        #consulto stock
        stock=consultar_stock(producto[0],id_talle)
        if stock < cantidad:
         print("Lo sentimos,no disponemos de suficiente stock para su pedido,intente con otro producto")
         continue
        else:
            nuevo_stock= stock-cantidad
            producto_talle=Producto_talle()
            producto_talle.ID_producto= producto[0]
            producto_talle.ID_talle= id_talle
            producto_talle.stock= nuevo_stock
            modify_stock(producto_talle)
        #calculo subtotal
        subtotal= cantidad * producto[3]
         # Agrega el detalle a la lista de detalles
        Lista_detalles.append((producto[0],id_talle, cantidad, subtotal))
        agregar_producto =input("¿Desea agregar otro producto al pedido? (Sí/No): ").strip().lower()
        if agregar_producto == "no":
         return Lista_detalles
         break
 except ValueError as error:
     cancelar_detalle(Lista_detalles)
     print("Error:", error)
     
 
     
     
def cancelar_pedido(id):
 try:
    pedidos=listar_pedidos(id)
    if pedidos is None:
        print("Usted no realizo ningun pedido aun")
        return
    else:
     print("ESTOS SON SUS PEDIDOS")
     encabezados = ["Nro pedido","Subtotal","Cantidad","ID Talle","Talle","ID_producto","Nombre producto","Fecha","Total"]
     print(tabulate(pedidos, headers=encabezados, tablefmt="pretty"))
     try:
         while True:
          id_pedido=int(input("Ingrese el numero del pedido que desea cancelar: "))
          if validacion_numero(id_pedido,"Numero de pedido"):
           continue
          else:
             break
     except:
         raise ValueError("El numero de pedido no puede ser un caracter o estar vacio")
    venta=buscar_pedido(id_pedido)
    if venta is None:
        return print("Lo sentimos,no existe ese pedido a su nombre")
    elif venta[4] =="CANCELADO":
     return print("el pedido ya se encontraba cancelado")
    else:
     estado = "cancelado"
     valor=modificar_estado(estado,id_pedido)
     if valor is True:
      try:
    #en caso de cancelar el pedido,devuelvo los productos que estaban en el pedido al stock
        detalles= buscar_detalle(id_pedido)
        for detalle in detalles:
            producto_talle= Producto_talle()
            producto_talle.ID_producto=detalle[2]
            producto_talle.ID_talle= detalle[3]
            cantidad= detalle[4]
            stock=consultar_stock(producto_talle.ID_producto,producto_talle.ID_talle)
            nuevo_stock= cantidad + stock
            producto_talle.stock=nuevo_stock
            modify_stock(producto_talle)
      except ValueError as error:
       print("Error:", error)
       return
    eliminar_detalles_pedido(id_pedido)
    return print("El pedido fue cancelado")
 except ValueError as error:
  print("Error:", error)
  
  
def listar_pedidos_cliente(id):
    try:
        resultado=listar_pedidos(id)
        if resultado is None:
         print("Usted no realizo ningun pedido aun")
         return
        else:
         print("Estos son sus pedidos")
         encabezados = ["ID pedido","Subtotal","Cantidad","ID Talle","Talle","ID_producto","Nombre producto","Fecha","Total"]
         print(tabulate(resultado, headers=encabezados, tablefmt="pretty"))
        
    except ValueError as error:
     print("Error:", error)
     
     
 #metodo a utilizar en caso de que ocurra un error en la creacion del pedido    
def cancelar_detalle(Lista_detalles):
    for lista in Lista_detalles:
         producto_talle=Producto_talle()
         producto_talle.ID_producto= lista[0]
         producto_talle.ID_talle= lista[1]
         nuevo_stock= consultar_stock(producto_talle.ID_producto, producto_talle.ID_talle) + lista[2]
         producto_talle.stock= nuevo_stock
         modify_stock(producto_talle)
         
         
def ventas():
     try:
        resultado=listar_ventas()
        if resultado is None:
         print("No existe ningun pedido aun")
         return
        else:
         print("Estas son las ventas historicas")
         encabezados = ["ID usuario","ID pedido","Subtotal","Cantidad","ID Talle","Talle","ID_producto","Nombre producto","Fecha","Total"]
         print(tabulate(resultado, headers=encabezados, tablefmt="pretty"))
         total_ventas = calcular_total_ventas() 
         print("EL TOTAL DE VENTAS HISTORICO FUE :", total_ventas)
     except ValueError as error:
      print("Error:", error)
  
      
 #funcion para calcular las ventas del mes con detalle de productos y talles vendidos    
def listar_ventas_con_detalle():
    try:
     while True:
          mes= input("Ingrese el año y el mes del que desea consultar las ventas en formato 'YYYY-MM': ")
          if not es_fecha_valida(mes):
           print("Fecha no válida. debes ingresar un año y mes válidos en formato 'YYYY-MM'.")
           continue
          else:
            break
     ventas = listar_ventas_detalladas(mes)
     if ventas is not None:
         print("Estas fueron las ventas de ese mes")
         encabezados = ["ID usuario","ID pedido","Subtotal","Cantidad","ID Talle","Talle","ID_producto","Nombre producto","Fecha","Total"]
         print(tabulate(ventas, headers=encabezados, tablefmt="pretty")) 
         total_ventas = calcular_total_mensual(mes) 
         print("TOTAL DE VENTAS EN EL MES:", total_ventas) 
     else:
         print("No se encontraron ventas para el mes ingresado.")
         
    except ValueError:
     print("Formato de fecha incorrecto. Asegúrate de ingresar un año y mes válidos en formato 'YYYY-MM'.")
     
     
#funcion para calcular las ventas mensuales   
def calcular_ventas_mensuales():
    try:
     while True:
          mes= input("Ingrese el año y el mes del que desea consultar las ventas en formato 'YYYY-MM': ")
          if not es_fecha_valida(mes):
           print("Fecha no válida. debes ingresar un año y mes válidos en formato 'YYYY-MM'.")
           continue
          else:
            break
     ventas = listar_ventas_por_mes(mes)
     if ventas is not None:
         print("Estas fueron las ventas de ese mes")
         encabezados = ["ID usuario","ID pedido","Fecha","Total"]
         print(tabulate(ventas, headers=encabezados, tablefmt="pretty")) 
         total_ventas = calcular_total_mensual(mes) 
         print("TOTAL DE VENTAS EN EL MES:", total_ventas) 
     else:
         print("No se encontraron ventas para el mes ingresado.")
         
    except ValueError:
     print("Formato de fecha incorrecto. Asegúrate de ingresar un año y mes válidos en formato 'YYYY-MM'.")
     
     
def calcular_ventas_segun_pago():
    try:
      while True:
          mes= input("Ingrese el año y el mes del que desea consultar las ventas en formato 'YYYY-MM': ")
          if not es_fecha_valida(mes):
           print("Fecha no válida. debes ingresar un año y mes válidos en formato 'YYYY-MM'.")
           continue
          else:
            break
      metodos=formas_de_pago()
      if metodos:
       print("Estas son las forma de pagos que trabajamos actualmente")
       encabezados = ["Metodo de pago"]
       print(tabulate(metodos, headers=encabezados, tablefmt="pretty"))
      forma_de_pago=input("Ingrese la forma de pago que desea consultar: ")
      resultado=calcular_mensual_segun_forma_de_pago(mes, forma_de_pago)
      if resultado is not None:
       encabezados = ["ID Pedido", "Forma de Pago", "Total", "Mes", "Venta Mensual de esta forma de pago"]
       print(tabulate(resultado, headers=encabezados, tablefmt="pretty"))
       total_ventas = calcular_total_mensual_por_metodo_de_pago(mes,forma_de_pago) 
       print(f"EL TOTAL DE VENTAS EN EL MES MEDIANTE {forma_de_pago} COMO FORMA DE PAGO,FUE DE:", total_ventas)
      else:
       print("No se encontraron resultados para el metodo de pago seleccionado.")   
    except ValueError:
     print("Formato de fecha incorrecto. Asegúrate de ingresar un año y mes válidos en formato 'YYYY-MM'.")
     
     
def calcular_ventas_anuales():
    try:
     while True:
          year= input("Ingrese el año del que desea consultar las ventas en formato 'YYYY': ")
          if not fechavalida_anio(year):
           print("Fecha no válida. debes ingresar un año y mes válidos en formato 'YYYY'.")
           continue
          else:
            break
     ventas = listar_ventas_por_year(year)
     if ventas is not None:
         print("Estas fueron las ventas de ese año")
         encabezados = ["ID usuario","ID pedido","Fecha","Total"]
         print(tabulate(ventas, headers=encabezados, tablefmt="pretty")) 
         total_ventas = calcular_total_anual(year) 
         print("TOTAL DE VENTAS EN EL AÑO:", total_ventas) 
     else:
         print("No se encontraron ventas para el año ingresado.")
         
    except ValueError:
     print("Formato de fecha incorrecto. Asegúrate de ingresar un año válido en formato 'YYYY'.")
     
     
def listar_pedidos_cancelado():
    try:
         while True:
          mes= input("Ingrese el año y el mes del que desea consultar las ventas en formato 'YYYY-MM': ")
          if not es_fecha_valida(mes):
           print("Fecha no válida. debes ingresar un año y mes válidos en formato 'YYYY-MM'.")
           continue
          else:
            break
         resultado=ver_pedidos_cancelados(mes)
         if resultado is not None:
          print("Estos pedidos fueron cancelados en ese mes")
          encabezados = ["ID DEL PEDIDO","FECHA","ID USUARIO","TOTAL","ESTADO"]
          print(tabulate(resultado, headers=encabezados, tablefmt="pretty")) 
         else:
             print("No se cancelaron pedidos en el mes consultado")
            
    except ValueError:
     print("Formato de fecha incorrecto. Asegúrate de ingresar un año y mes válidos en formato 'YYYY-MM'.")