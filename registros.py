
def Mostrar_datos():
    Nombre = str(input("Ingrese su nombre y apellido: "))
    codigo = str(input("Ingrese su código: "))
    Consulta = str(input("Ingrese el tipo de consulta:"))
    Descripcion = str(input("Desciba de forma breve su consulta:"))
    return Nombre, codigo, Consulta, Descripcion


Mostrar_datos()