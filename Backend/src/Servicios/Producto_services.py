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
        nombre=input("Por favor,ingrese el nombre del nuevo producto: ")
        #valido que el campo no este vacio
        validacion_campo(nombre)
        exists =buscar_producto(nombre)
        if exists is None:
         producto1.nombre_producto = nombre
        else:
            return print("El producto ya existe en nuestra base de datos, si desea modificar algo de este producto,ingrese en la opcion correspondiente")
        descripcion=input("Ingrese una descripcion del producto: ")
        validacion_campo(descripcion)
        producto1.descripcion= descripcion
        precio=float(input("Ingrese el precio (solo numeros) por unidad: ")) 
        validacion_numero(precio,"PRECIO")
        producto1.precio = precio
        talle1= Talle()
        talle =input("Indique el talle del producto: ")
        validacion_campo(talle)
        talle1.talle = talle
        prod_talle= Producto_talle()
        stock =float(input("Ingrese la cantidad (solo numeros) en stock del talle de este producto: "))
        if stock < 0:
         raise ValueError(f"El Stock no debe ser menor a 0")
        id_producto=crear_product(nombre,descripcion,precio)
        producto1.ID_producto= id_producto
        id_talle = buscar_id_talle(talle)
        if id_talle is None:
            return print("No se encontro ese talle en nuestra base de datos,por favor,agrega primero el talle")
        talle1.ID_talle= id_talle
        prod_talle.ID_producto= id_producto
        prod_talle.ID_talle= id_talle
        prod_talle.stock = stock
        id_final=insert_producto_talle(id_producto,id_talle,stock)
        print (f"El producto: {producto1.nombre_producto} de TALLE: {talle1.talle} fue agregado correctamente a {producto1.precio} pesos")
        while True:
            respuesta =input("¿Desea cargar otro talle y stock  para este mismo producto? (Sí/No): ").strip().lower()
            
            if respuesta == "no":
                break
            elif respuesta == "sí" or respuesta == "si":   
                talle2 = input("Indique el talle del producto: ")
                validacion_campo(talle2)
                talle_nuevo = Talle()
                talle_nuevo.talle = talle2
                stock = float(input("Ingrese la cantidad (solo números) en stock del talle de este producto: "))
                if stock < 0:
                    raise ValueError(f"El Stock no debe ser menor a 0")
                id_talle2 = buscar_id_talle(talle2)
                if id_talle2 is None:
                    return print("No se encontró ese talle en nuestra base de datos, por favor, agregue primero el talle")
                talle_nuevo.ID_talle = id_talle2
                prod_talle2= Producto_talle()
                prod_talle2.ID_talle = id_talle2
                prod_talle2.stock = stock
                result = buscar_id_producto_talle(id_talle2,id_producto)
                if result is None:
                 insert_producto_talle(id_producto, id_talle2, stock)
                else:
                 nuevo_stock = stock
                 modify_stock(nuevo_stock,id_producto,id_talle2)
                print (f"El producto: {producto1.nombre_producto} de TALLE: {talle_nuevo.talle} fue agregado correctamente a {producto1.precio} pesos")
            else:
                print("Respuesta no válida. Por favor, responda 'Sí' o 'No'.")  
        
    except ValueError as error:
     print("Error:", error)
     
     
#metodo para modificar el stock de un determinado talle de un producto existente
def modificar_stock_talle():
    try:
        p1 =Producto_talle()
        nombre=input("Por favor,ingrese el nombre del  producto que desea modificar su stock: ")
        validacion_campo(nombre)
        producto_id =buscar_producto(nombre)
        if producto_id is None:
         return print("El producto no existe en nuestra base de datos, debera crearlo primero ")
        p1.ID_producto = producto_id
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
        productoTalle= buscar_id_producto_talle(talleID,producto_id)
        if productoTalle is None:
            #si no existe se lo persisto y le asigno su stock
            insert_producto_talle(producto_id,talleID,stock)
            return print(f"El PRODUCTO: {nombre},de TALLE: {talle} tiene ahora {p1.stock} unidades")     
        else:
           #termino de setear el objeto producto_talle para cuando necesite conectar con el front pueda enviar el objeto como json
          p1.ID_producto_talle = productoTalle[0]
           #si existe solo le cambio el stock
          nuevo_stock=  stock + productoTalle[3]
          p1.stock = nuevo_stock
        modify_stock(nuevo_stock,producto_id,talleID)
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
        modify_nombre_producto(nombre_nuevo,id)
    
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
        p1.ID_producto = producto_id
        talle =input("Ingrese el talle del producto ")
        validacion_campo(talle)
        talleID =buscar_id_talle(talle)
        if talleID is None:
            return print("No se encontro el talle en nuestra base de datos.")
        resultado=consultar_stock(producto_id,talleID)
        if resultado is not None:
         stock = int(resultado[0])
         return print(f"el Stock del producto {nombre} de talle {talle} es = {resultado}")
        else:
           print("No se encontro el producto de ese talle en la base de datos.")
          
          
            
    except ValueError as error:
     print("Error:", error)
     

def listar_productos():
 try:
    productos =all_products()
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
        
        talle =input("Ingrese el talle del producto: ")
        validacion_campo(talle)
        talleID =buscar_id_talle(talle)
        if talleID is None:
            return print("No se encontro el talle en nuestra base de datos.")
        stock= 0
        modify_stock(stock,producto_id,talleID)
        print(f"El producto {nombre} de Talle {talle}, ya no figura en la lista de nuestro productos a la venta")
        
    except ValueError as error:
     print("Error:", error)