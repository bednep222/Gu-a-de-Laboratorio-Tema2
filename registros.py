def Validar_nombre(Nombre):
  Nombre = Nombre.strip()
  if Nombre == "":
    print("Ingrese un nombre valido e intentalo nuevamente")
    return False
  else:
    return True

def Validar_codigo(Codigo):
  Longitud_codigo = 8
  Codigo = Codigo.strip()
  if len(Codigo) != Longitud_codigo:
    print("El codigo no puede estar vacio y debe tener 8 caracteres, ingrese su codigo nuevamente")
    return False
  else:
   return True 

def Validar_tipoconsulta(Consulta):
 Consulta = Consulta.strip().lower()
 tipos_consulta = ["matricula", "pagos", "constancias", "certificaciones", "otros"]
 if Consulta not in tipos_consulta:
  print("El tipo de consulta no es válido, ingrese un tipo de consulta válido")
  return False
 else:
  return True

def Prioridad(Consulta):
    Consulta = Consulta.strip().lower()
    if Consulta == "matricula":
     return "Prioridad Alta"
    elif Consulta == "pagos":
       return "Prioridad Alta"
    elif Consulta == "constancias":
     return "Prioridad Media"
    elif Consulta == "certificaciones":
     return "Prioridad Media"
    elif Consulta == "otros":
      return "Prioridad Baja"
    else:
      return "Error de prioridad"

def Resumen_datos(Nombre, codigo, Consulta, Descripcion, Nivel):
  print("-Solicitud-")
  print("Nombre: ", Nombre)
  print("Codigo: ", codigo)
  print("Consulta: ", Consulta)
  print("Descripcion: ", Descripcion)
  print("Nivel:", Nivel)

    
def Mostrar_datos():
    Nombre = str(input("Ingrese su nombre: "))
    while not Validar_nombre(Nombre):
      Nombre = str(input("Ingrese su nombre: "))

    codigo = str(input("Ingrese su código: "))
    codigo = codigo.strip()
    while not Validar_codigo(codigo):
      codigo = str(input("Ingrese su código: "))
      codigo = codigo.strip()

    Consulta = str(input("Ingrese el tipo de consulta:"))
    Consulta = Consulta.strip().lower()
    while not Validar_tipoconsulta(Consulta):
      Consulta = str(input("Ingrese el tipo de consulta: "))
      Consulta = Consulta.strip().lower()
    nivel = Prioridad(Consulta)
    print(nivel)
    Descripcion = str(input("Describa de forma breve su consulta: "))
    return Nombre, codigo, Consulta, Descripcion, nivel

Nombre, codigo, Consulta, Descripcion, nivel = Mostrar_datos()
Mostrar_datos(Nombre, codigo, Consulta, Descripcion, nivel)