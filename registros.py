def Validar_nombre(Nombre):
  Nombre = Nombre.strip()
  if Nombre == "":
    print("Ingrese un nombre valido e intentalo nuevamente")
    return False
  else:
    return True

def Validar_codigo(Codigo):
  Longitud_codigo = 8
  if len(Codigo) != Longitud_codigo:
    print("El codigo no puede estar vacio y debe tener 8 caracteres, ingrese su codigo nuevamente")
    return False
  else:
   return True 

def Validar_tipoconsulta(Consulta):
 consulta = consulta.strip().lower()
 tipos_consulta = ["matricula", "pagos", "constancias", "certificaciones", "otros"]
 if Consulta not in tipos_consulta:
  print("El tipo de consulta no es válido, ingrese un tipo de consulta válido")
  return False
 else:
  return True

def Prioridad(Consulta):
    Texto = "Alta","Media","Baja"
    if Consulta == "matricula":
     return "Alta"
    elif Consulta == "pagos":
       return "Alta"
    elif Consulta == "constancias":
     return "Media"
    elif Consulta == "certificaciones":
     return "Media"
    elif Consulta == "otros":
      return "Baja"
    else:
      return "Error de prioridad"
    
def Mostrar_datos():
    Nombre = str(input("Ingrese su nombre: "))
    while not Validar_nombre(Nombre):
      Nombre = str(input("Ingrese su nombre: "))
    codigo = str(input("Ingrese su código: "))
    while not Validar_codigo(codigo):
      codigo = str(input("Ingrese su código: "))
    Consulta = str(input("Ingrese el tipo de consulta:"))
    while not Validar_tipoconsulta(Consulta):
      Consulta = str(input("Ingrese el tipo de consulta: "))
      Prioridad(Consulta)
      print (nivel)
  
    Descripcion = str(input("Desciba de forma breve su consulta:"))
    return Nombre, codigo, Consulta, Descripcion, Prioridad

Mostrar_datos()
