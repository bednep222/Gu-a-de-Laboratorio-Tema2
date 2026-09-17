
def Validar_codigo(Codigo):
  Longitud_codigo = 8
  if Codigo == "" or len(Codigo) > Longitud_codigo:
   print("El codigo no puede estar vacio o tener mas de 8 caracteres")
   return False
  else:
   return True 



def Mostrar_datos():
  Nombre = str(input("Ingrese su nombre y apellido: "))
  codigo = str(input("Ingrese su código: "))
  while not Validar_codigo(codigo):
   print("Ingrese su codigo nuevamente")
   codigo = str(input("Ingrese su código: "))
  Consulta = str(input("Ingrese el tipo de consulta:"))
  Descripcion = str(input("Desciba de forma breve su consulta:"))
  return Nombre, codigo, Consulta, Descripcion

Mostrar_datos()