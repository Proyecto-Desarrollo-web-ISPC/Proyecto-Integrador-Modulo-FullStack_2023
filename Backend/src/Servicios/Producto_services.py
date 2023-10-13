from Entidades.Producto import *
from Entidades.Talle import *
from Entidades.Producto_talle import *
from Validaciones.validacion_campos import *
from Repositorio.Producto_repositorio import *
from tabulate import tabulate

#metodo para crear producto
def crear_producto ():
    try:
        #instancio un producto para ir seteando sus atributos
        producto1= Producto()
        while True:
         nombre=input("Por favor,ingrese el nombre del nuevo producto: ")
        #valido que el campo no este vacio
         if validacion_campo(nombre):
             continue
         else:
             break
        exists =buscar_producto(nombre)
        if exists is None:
         producto1.nombre_producto = nombre
        else:
            return print("El producto ya existe en nuestra base de datos, si desea modificar algo de este producto,ingrese en la opcion correspondiente")
        while True:
         descripcion=input("Ingrese una descripcion del producto: ")
         if validacion_campo(descripcion):
             continue
         else:
             break
        producto1.descripcion= descripcion
        try:
         while True:
          precio=float(input("Ingrese el precio (solo numeros) por unidad: ")) 
          if validacion_numero(precio,"PRECIO"):
             continue
          else:
             break
        except:
            print("El campo precio debe contener solo numeros y no puede estar vacio")
        producto1.precio = precio
        talle1= Talle()
        while True:
         lista=listar_talles()
         if lista:
          print("*****ESTA ES NUESTRA LISTA DE TALLES*****")
          encabezados = ["TALLES"]
         print(tabulate(lista, headers=encabezados, tablefmt="pretty"))
         talle =input("Indique el talle del producto: ")
         if validacion_campo(talle):
             continue
         else:
             break
        talle1.talle = talle
        prod_talle= Producto_talle()
        try:
         while True:
          stock =float(input("Ingrese la cantidad (solo numeros) en stock del talle de este producto: "))
          if stock < 0:
           print(f"El Stock no debe ser menor a 0")
           continue
          else:
             break
        except:
           print("El campo stock debe contener numeros y no puede estar vacio")
        id_talle = buscar_id_talle(talle)
        if id_talle is None:
         return print("No se encontro ese talle en nuestra base de datos,por favor,agrega primero el talle")
        id_producto=crear_product(producto1)
        producto1.ID_producto= id_producto
        talle1.ID_talle= id_talle
        prod_talle.ID_producto= producto1.ID_producto
        prod_talle.ID_talle= id_talle
        prod_talle.stock = stock
        id_final=insert_producto_talle(prod_talle)
        prod_talle._ID_producto_talle= id_final
        print (f"El producto: {producto1.nombre_producto} de TALLE: {talle1.talle} fue agregado correctamente a {producto1.precio} pesos")
        while True:
            respuesta =input("¿Desea cargar otro talle y stock  para este mismo producto? (Sí/No): ").strip().lower()
            
            if respuesta == "no":
                print("Los productos fueron agregados correctamente,gracias por usar nuestro sistema")
                break
            elif respuesta == "sí" or respuesta == "si":  
                while True: 
                 talle2 = input("Indique el talle del producto: ")
                 if validacion_campo(talle2):
                     continue
                 else:
                     break
                talle_nuevo = Talle()
                talle_nuevo.talle = talle2
                try:
                 while True:
                  stock = float(input("Ingrese la cantidad (solo números) en stock del talle de este producto: "))
                  if stock < 0:
                    print(f"El Stock no debe ser menor a 0")
                    continue
                  else:
                    break
                except:
                 print("El campo stock debe contener solo numeros y no puede estar vacio")
                id_talle2 = buscar_id_talle(talle2)
                if id_talle2 is None:
                    return print("No se encontró ese talle en nuestra base de datos, por favor, agregue primero el talle")
                talle_nuevo.ID_talle = id_talle2
                prod_talle2= Producto_talle()
                prod_talle2.ID_talle = id_talle2
                prod_talle2.stock = stock
                prod_talle2.ID_producto= id_producto
                result = buscar_id_producto_talle(id_talle2,id_producto)
                if result is None:
                 insert_producto_talle(prod_talle2)
                else:
                 nuevo_stock = stock
                 modify_stock(nuevo_stock,id_producto,id_talle2)
                print (f"El producto: {producto1.nombre_producto} de TALLE: {talle_nuevo.talle} fue agregado correctamente a {producto1.precio} pesos")
            else:
                print("Respuesta no válida. Por favor, responda 'Sí' o 'No'.")  
        
    except ValueError as error:
     print("Error:", error)
     
     
#metodo para modificar el stock de un determinado talle de un producto existente
#este metodo utilizo cuando por ej creo un producto y le asigno un talle y stock,y sali del metodo crear producto.
#de manera que con esta funcion,puedo seguir agregando talles y stock a un producto creado previamente
def modificar_stock_talle():
    try:
        p1 =Producto_talle()
        nombre=input("Por favor,ingrese el nombre del  producto al que desea agregar talle y stock: ")
        validacion_campo(nombre)
        producto_id =buscar_producto(nombre)
        if producto_id is None:
         return print("El producto no existe en nuestra base de datos, debera crearlo primero ")
        p1.ID_producto = producto_id[0]
        talle =input("Ingrese el talle del producto: ")
        validacion_campo(talle)
        talleID =buscar_id_talle(talle)
        if talleID is None:
            return print("No se encontro el talle en nuestra base de datos.")

        p1.ID_talle = talleID
        stock=int(input("ingrese el nuevo Stock del producto: "))
        validacion_numero(stock,"STOCK")
        p1.stock = stock
        #busco el id de la tabla producto_talle para ver si el talle  existe en ese producto
        productoTalle= buscar_id_producto_talle(p1.ID_talle,p1.ID_producto)
        if productoTalle is None:
            #si no existe ese talle para ese producto lo persisto y le asigno su stock
            insert_producto_talle(p1)
            return print(f"El PRODUCTO: {nombre},de TALLE: {talle} tiene ahora {p1.stock} unidades")     
        else:
           #termino de setear el objeto producto_talle para cuando necesite conectar con el front pueda enviar el objeto como json
          p1.ID_producto_talle = productoTalle[0]
           #si existe solo le cambio el stock
          nuevo_stock=  stock + productoTalle[3]
          p1.stock = nuevo_stock
        modify_stock(p1)
        print (f"El PRODUCTO: {nombre},de TALLE: {talle} tiene ahora {p1.stock} unidades")
            
    except ValueError as error:
     print("Error:", error)
     
     
def cambiar_nombre_producto():
    try:
        nombre=input("Por favor,ingrese el nombre del  producto que desea modificar: ")
        validacion_campo(nombre)
        id =buscar_producto(nombre)
        if id is None:
         return print("El producto no existe en nuestra base de datos,ingrese en la opcion crear producto nuevo")
        nombre_nuevo=input("ingrese el nuevo nombre del producto: ")
        validacion_campo(nombre)
        modify_nombre_producto(nombre_nuevo,id[0])
    
    except ValueError as error:
     print("Error:", error)
     
     
def consultar_stock_producto():
    try:
        p1 =Producto_talle()
        nombre=input("Por favor,ingrese el nombre del  producto: ")
        validacion_campo(nombre)
        producto_id =buscar_producto(nombre)
        if producto_id is None:
         return print("El producto no existe en nuestra base de datos, debera crearlo primero ")
        p1.ID_producto = producto_id[0]
        talle =input("Ingrese el talle del producto ")
        validacion_campo(talle)
        talleID =buscar_id_talle(talle)
        if talleID is None:
            return print("No se encontro el talle en nuestra base de datos.")
        p1.ID_talle=talleID
        resultado=consultar_stock(p1.ID_producto,p1.ID_talle)
        if resultado is not None:
         stock = resultado
         return print(f"el Stock del producto {nombre} de talle {talle} es = {resultado} unidades")
        else:
           print("No se encontro el producto de ese talle en la base de datos.")
          
          
            
    except ValueError as error:
     print("Error:", error)
     

def listar_productos_talle():
 try:
    nombre=input("ingrese el nombre del producto: ")
    productos =all_products(nombre)
    if productos:
         encabezados = [ "Nombre producto", "Precio", "Talle","Stock disponible"]
         print(tabulate(productos, headers=encabezados, tablefmt="pretty"))
    else:
      print("No se encontraron resultados.")
  
    
 except ValueError as error:
     print("Error:", error)
     
#se realiza un soft delete,ya que hay varias tablas relacionadas al producto
def eliminar_producto():
    try:
        nombre=input("Por favor,ingrese el nombre del  producto que desea eliminar: ")
        validacion_campo(nombre)
        producto_id =buscar_producto(nombre)
        if producto_id is None:
         return print("El producto no existe en nuestra base de datos")
        id=producto_id[0]
        talle =input("Ingrese el talle del producto: ")
        validacion_campo(talle)
        talleID =buscar_id_talle(talle)
        if talleID is None:
            return print("No se encontro el talle en nuestra base de datos.")
        stock= 0
        p_talle=Producto_talle()
        p_talle.ID_producto=id
        p_talle.ID_talle=talleID
        p_talle.stock= stock
        modify_stock(p_talle)
        print(f"El producto {nombre} de Talle {talle}, ya no figura en la lista de nuestro productos a la venta")
        
    except ValueError as error:
     print("Error:", error)
     
     
     
def listar_todos_productos():
    try:
        productos =listarProductos()
        if productos:
         encabezados = [ "Nombre producto", "Precio"]
         print(tabulate(productos, headers=encabezados, tablefmt="pretty"))
        else:
         print("No se encontraron resultados.")
        
    except ValueError as error:
     print("Error:", error)
        
     
def mostrar_descripcion():
    try:
        productos =listar_descripcion()
        for nombre_producto, descripcion in productos:
         print("Camiseta:", nombre_producto)
         print("Descripción:", descripcion)
         print("-" * 30)
    except ValueError as error:
     print("Error:", error)
     
     
def modificar_precio_producto():
 try:
     while True:
      nombre=input("Ingrese el nombre del producto que desea modificar: ")
      if validacion_campo(nombre):
        continue
      id=buscar_producto(nombre)
      if id is None:
       return print("El producto no existe en nuestra base de datos")
      precio=float(input("Ingrese el nuevo precio del producto: "))
      if validacion_numero(precio,"PRECIO"):
       continue
      modify_precio(precio,id[0])
      break
 except ValueError as error:
     print("Error:", error) 
    
    
def modificar_descripcion():
 try:
     while True:
      nombre=input("Ingrese el nombre del producto que desea modificar: ")
      if validacion_campo(nombre):
        continue
      id=buscar_producto(nombre)
      if id is None:
       return print("El producto no existe en nuestra base de datos")
      descripcion=input("Ingrese la nueva descripcion del producto: ")
      if validacion_campo(descripcion):
       continue
      cambiar_descripcion(descripcion,id[0])
      break
 except ValueError as error:
     print("Error:", error)     
    