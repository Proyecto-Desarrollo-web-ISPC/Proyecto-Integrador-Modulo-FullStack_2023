
def validacion_campo(args):
    if not args:
        raise ValueError("el campo no puede estar vacío,por favor completa el campo")
    
    
def validacion_caracter(args,campo):
    if not args.isalpha():
     raise ValueError(f"El campo {campo}  deben contener solo caracteres")
 
 
def validacion_numero(args,campo):
    if args <= 0:
        raise ValueError(f"El campo {campo} debe contener solo números")
