from datetime import datetime
import re
def validacion_campo(args):
    if not args:
        print("El campo no puede estar vacío, por favor completa el campo.")
        return True  
    else:
        return False 
     
def validacion_caracter(args,campo):
     if not args.replace(" ", "").isalpha():
      print(f"El campo {campo}  deben contener solo caracteres")
      return True
     else:
        return False
 
 
def validacion_numero(args,campo):
    if args <= 0:
      print(f"El campo {campo} debe contener solo números")
      return True
    else:
        return False
 
def es_fecha_valida(fecha):
    try:
        datetime.strptime(fecha, '%Y-%m')
        return True
    except ValueError:
        return False

def fechavalida_anio(fecha):
    try:
        datetime.strptime(fecha,'%Y')
        return True
    except ValueError:
        return False
    
def validar_correo(correo):
    patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    
    if re.match(patron, correo):
        return True
    else:
        return False