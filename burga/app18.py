
import libreria
def dato1():

    nombre=libreria.pedir_nombre("nombre")
    contenido=nombre+"\n"
    libreria.guardar_datos("info.txt",contenido,"a")
    print("datos guardados")
def dato2():
    nacimiento=libreria.pedir_año("IGV:")
    nombre=libreria.pedir_nombre("nombre")
    contenido=nacimiento+"-"+str(nombre)+"\n"
    libreria.guardar_datos("info.txt",contenido,"a")
    print("datos guardados")
def verDatos():
    datos=libreria.obtener_datos("info.txt")
    if(datos!=""):
        print(datos)
    else:
        print("archivo sin datos ")

def opc_nombre():
    opc=0
    max=3
    while(opc!=max):
        print("#########DATO1###########")
        print("#1.ingresar su nombre: ")
        print("#2.ver datos")
        print("#3.salir")
        print("########################")
        opc=libreria.pedir_numero("ingrese subopcion",1,3)
        if(opc==1):
           dato1()
        if(opc==2):
           verDatos()

def opc_nacimiento():
    opc=0
    max=3
    while(opc!=max):
        print("#########DATO2###########")
        print("#1.ingresar el año de nacimiento: ")
        print("#2.ver datos")
        print("#3.salir")
        print("########################")
        opc=libreria.pedir_numero("ingrese subopcion",1,3)
        if(opc==1):
           dato2()
        if(opc==2):
           verDatos()

opc=0
max=3
while(opc!=max):
    print("#########MENU###########")
    print("#1.ingresar nombre:  ")
    print("#2.mingresar año de nacimiento: ")
    print("#3.salir")
    print("########################")
    opc=libreria.pedir_numero("ingrese opcion",1,3)
    if(opc==1):
        opc_nombre()
    if(opc==2):
        opc_nacimiento()
#fin
print("fin del programa")
