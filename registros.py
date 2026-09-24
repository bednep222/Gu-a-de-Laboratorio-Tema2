# [Req. 6]:
def Validar_nombre(Nombre):
  Nombre = Nombre.strip()
  if Nombre == "":
   print("El dato no puede estar vacio, intentalo nuevamente")
   return False
  else:
   return True
# [Req. 2]:
def Validar_codigo(Codigo):
  Longitud_codigo = 8
  Codigo = Codigo.strip()
  if len(Codigo) != Longitud_codigo:
    print("El codigo no puede estar vacio y debe tener 8 caracteres, ingrese su codigo nuevamente")
    return False
  else:
   return True 
# [Req. 3]:
def Validar_tipoconsulta(Consulta):
 Consulta = Consulta.strip().lower()
 tipos_consulta = ["matricula", "pagos", "constancias", "certificaciones","plataforma","otros"]
 if Consulta not in tipos_consulta:
  print("El tipo de consulta no es válido, ingrese un tipo de consulta válido")
  return False
 else:
  return True
# [Req. 5]:
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
    elif Consulta == "plataforma":
      return "Prioridad Media"
    elif Consulta == "otros":
      return "Prioridad Baja"
    else:
      return "Error de prioridad"

# [Req. 6]:
def Validar_descripcion(Descripcion):
    Descripcion = Descripcion.strip()
    if Descripcion == "":
      print("El dato no puede estar vacio, intentalo nuevamente")
      return False
    else:
      return True
# [Req. 7]:
def Resumen_datos(Nombre, codigo, Consulta, Descripcion, Nivel,):
  print("-Solicitud-")
  print("Nombre: ", Nombre)
  print("Codigo: ", codigo)
  print("Consulta: ", Consulta)
  print("Descripcion: ", Descripcion)
  print("Nivel:", Nivel)
# [Req. 4]:
def mostrar_menu():
  print("1. Registrar solicitud")
  print("2. Ver ultima solicitud")
  print("3. Salir")

# [Req. 1,8,9]:  
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
    Descripcion = Descripcion.strip()
    while not Validar_descripcion(Descripcion):
      Descripcion = str(input("Describa de forma breve su consulta: "))
      Descripcion = Descripcion.strip()
    return Nombre, codigo, Consulta, Descripcion, nivel

# [Req. 8, 9, 10, 11]
ult_nombre = ""
ult_codigo = ""
ult_consulta = ""
ult_descripcion = ""
ult_nivel = ""

while True:
    mostrar_menu()
    opcion = input("Elija una opcion: ").strip() # Solo una lectura de input
    if opcion == "1":
        Nombre, codigo, Consulta, Descripcion, nivel = Mostrar_datos()        
        ult_nombre = Nombre
        ult_codigo = codigo
        ult_consulta = Consulta
        ult_descripcion = Descripcion
        ult_nivel = nivel       
        Resumen_datos(Nombre, codigo, Consulta, Descripcion, nivel)
    elif opcion == "2":
        if ult_nombre != "":
            Resumen_datos(ult_nombre, ult_codigo, ult_consulta, ult_descripcion, ult_nivel)
        else:
            print("No hay solicitudes registradas aun.")
    elif opcion == "3":
        print("Saliendo...")
        break
    else:
        print("Opcion no valida")