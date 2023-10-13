from Servicios.Usuario_services import *
from Entidades.Usuario import *
from Servicios.Producto_services import *
from Servicios.Pedido_services import *


def menu_principal():
    continuar = True
    
    while continuar:
        opcion_correcta = False

        while not opcion_correcta:
            print("Bienvenido a nuestra tienda virtual CAMPEONES DEL MUNDO ")
            print("===== Menú Principal =====")
            print("1°- Ya soy cliente")
            print("2°- Registrarme como cliente nuevo")
            print("3°- Ingresar como administrador")
            print("4°- Salir")
            print("==========================")

            try:
                opcion = int(input("Seleccione una opción: "))

                if opcion == 1:
                    cliente= buscar_cliente()
                    if cliente:
                     print(f"bienvenido nuevamente {cliente.nombre} {cliente.apellido} {cliente._rol}")
                     menu_cliente(cliente.ID_usuario)
                    else:
                        continue
                    opcion_correcta = True
                elif opcion == 2:
                    user=crear_usuario(1)
                    if user:
                     menu_cliente(user.ID_usuario)
                    else:
                        continue
                    opcion_correcta = True
                elif opcion == 3:
                    menu_admin()
                    opcion_correcta = True
                elif opcion == 4:
                    continuar = False
                    opcion_correcta = True
                    print("¡MUCHAS GRACIAS POR USAR NUESTROS SERVICIOS, VUELVA PRONTO!")
                else:
                    print("Opción no válida. Por favor, seleccione una opción válida.")
            except ValueError:
                print("Entrada no válida. Ingrese un número válido.")
            except Exception as e:
                print(f"Ocurrió un error inesperado: {e}")
                
                
 #menu cliente
def menu_cliente(id):
    continuar = True

    while continuar:
        
        opcion_correcta = False

        while not opcion_correcta:
            print("===== Menú Cliente =====")
            print("1°- Realizar una compra")
            print("2°- Ver los productos de nuestra tienda")
            print("3°- Ver la historia de las camisetas que tenemos a la venta")
            print("4°- Consultar mis pedidos")
            print("5°- Cancelar un pedido")
            print("6°- Modificar mi email")
            print("7°- Modificar mi domicilio")
            print("8°- CERRAR SESION")
            print("==========================")
            
            try:  
             opcion = int(input("Por favor,seleccione una opción: "))
            
             if opcion == 1:
                 crear_pedido(id)
                 opcion_correcta = True
                 
             elif opcion == 2:
                 print("Estos son nuestros productos")
                 listar_todos_productos()
                 opcion_correcta = True
                 
             elif opcion == 3:
                mostrar_descripcion()
                opcion_correcta = True
                
             elif opcion == 4:
                listar_pedidos_cliente(id)
                opcion_correcta = True
                
             elif opcion == 5:
                cancelar_pedido(id)
                opcion_correcta = True
                
             elif opcion == 6:
                modificar_email(id)
                opcion_correcta = True
                
             elif opcion == 7:
                modificar_domicilio(id)
                opcion_correcta = True
             
             elif opcion == 8:
                continuar = False
                opcion_correcta = True
             else:
              print("Opción no válida. Por favor, seleccione una opción válida.")    
               
            except ValueError:   
             print("Entrada no válida. Ingrese un número válido.")
            except Exception as e:
             print(f"Ocurrió un error inesperado: {e}")
             
             
             
def menu_admin():
    continuar = True

    while continuar:
        
        opcion_correcta = False

        while not opcion_correcta:
            print("===== Menú admin =====")
            print("1°- Menu productos")
            print("2°- Menu ventas")
            print("3°- Volver al Menú Principal")
            print("==========================")
            
            try:  
             opcion = int(input("Por favor,seleccione una opción: "))
            
             if opcion == 1:
                 menu_productos()
                 opcion_correcta = True
                 
             elif opcion == 2:
                 menu_ventas()
                 opcion_correcta = True
                 
             elif opcion == 3:
                continuar = False
                opcion_correcta = True
             else:
              print("Opción no válida. Por favor, seleccione una opción válida.")    
               
            except ValueError:   
             print("Entrada no válida. Ingrese un número válido.")
            except Exception as e:
             print(f"Ocurrió un error inesperado: {e}")
             
             
def menu_productos():
    continuar = True

    while continuar:
        
        opcion_correcta = False

        while not opcion_correcta:
            print("===== Menú PRODUCTO =====")
            print("1°- Crear un producto")
            print("2°- Agregar talle y stock para un producto existente")
            print("3°- Modificar nombre de un producto")
            print("4°- Consultar stock de un producto")
            print("5°- Ver todos los productos de la tienda")
            print("6°- Consultar talles y stock disponibles de un producto")
            print("7°- Eliminar un producto")
            print("8°- Modificar el precio de un producto")
            print("9°- Modificar la descripcion de un producto")
            print("10°- Volver atras")
            print("==========================")
            
            try:  
             opcion = int(input("Por favor,seleccione una opción: "))
            
             if opcion == 1:
                 crear_producto()
                 opcion_correcta = True
                 
             elif opcion == 2:
                 modificar_stock_talle()
                 opcion_correcta = True
                 
             elif opcion == 3:
                cambiar_nombre_producto()
                opcion_correcta = True
                
             elif opcion == 4:
                consultar_stock_producto()
                opcion_correcta = True
                
             elif opcion == 5:
                listar_todos_productos()
                opcion_correcta = True
                
             elif opcion == 6:
                listar_productos_talle()
                opcion_correcta = True
                
             elif opcion == 7:
                eliminar_producto()
                opcion_correcta = True
             
             elif opcion == 8:
                modificar_precio_producto()
                opcion_correcta = True
                
             elif opcion == 9:
                modificar_descripcion()
                opcion_correcta = True
             
             elif opcion == 10:
                continuar = False
                opcion_correcta = True
             else:
              print("Opción no válida. Por favor, seleccione una opción válida.")    
               
            except ValueError:   
             print("Entrada no válida. Ingrese un número válido.")
            except Exception as e:
             print(f"Ocurrió un error inesperado: {e}")
             
             
def menu_ventas():
    continuar = True

    while continuar:
        
        opcion_correcta = False

        while not opcion_correcta:
            print("===== Menú Ventas =====")
            print("1°- Ver todos los pedidos y ventas historicas")
            print("2°- Buscar un cliente")
            print("3°- Calcular ventas mensuales")
            print("4°- listar y calcular ventas mensuales (con detalle de productos vendidos)")
            print("5°- calcular ventas mensuales segun metodos de pago")
            print("6°- calcular ventas anuales")
            print("7°- Listar pedidos cancelados en el mes")
            print("8°- Listar todos los clientes")
            print("9°- Volver al Menú admin")
            print("==========================")
            
            try:  
             opcion = int(input("Por favor,seleccione una opción: "))
            
             if opcion == 1:
                 ventas()
                 opcion_correcta = True
                 
             elif opcion == 2:
                 buscar_usuario_por_id()
                 opcion_correcta = True
                 
             elif opcion == 3:
                calcular_ventas_mensuales()
                opcion_correcta = True
                
             elif opcion == 4:
                listar_ventas_con_detalle()
                opcion_correcta = True
                
             elif opcion == 5:
                calcular_ventas_segun_pago()
                opcion_correcta = True
                
             elif opcion == 6:
                calcular_ventas_anuales()
                opcion_correcta = True
                
             elif opcion == 7:
                listar_pedidos_cancelado()
                opcion_correcta = True
                
             elif opcion == 8:
                listar_clientes()
                opcion_correcta = True
             
             elif opcion == 9:
                continuar = False
                opcion_correcta = True
             else:
              print("Opción no válida. Por favor, seleccione una opción válida.")    
               
            except ValueError:   
             print("Entrada no válida. Ingrese un número válido.")
            except Exception as e:
             print(f"Ocurrió un error inesperado: {e}")