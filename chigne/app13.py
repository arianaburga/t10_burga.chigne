# SUB MENUS 03
import libreria
opc=0             # opciones
max=3             # maximo de opciones

def subopcionA():
    print("Su genero es MASCULINO ")
def subopcionB():
    print("Su genero es FEMENINO ")

def opcionA():
     #El mombre que ingreses no debe contener numero
    a=libreria.validar_nombre(input("Ingrese nombre:"))
    print("El monbre del usurio es:"+str(a))
    contenido=a+"_"+"\n"
    libreria.agregar_datos("info.txt",contenido,"a")
    print("Nombre agregado")


def opcionB():
    #El sexo solo puede ser masculino o femenino
    opc=0
    max=3
    while (opc != max):
        print("#### SEXO DEL USUARIO ####")
        print("1. MASCULINO  ")
        print("2. FEMENINO  ")
        print("3. Exit")
        print("######################")
        opc=libreria.pedir_entero("OpcionA:",1,3)
        if (opc == 1):
            subopcionA()
        if (opc == 2):
            subopcionB()
        #Fin_submenuopc


while (opc != max):
    # 1. Imprecion del menu
    print("#######################")
    print("###      SEXO     ###")
    print("#######################")
    print("1. Nombre:            #")
    print("2. Sexo:               #")
    print("3. Salir              #")
    print("#######################")
    # 2. Eleccion de la opcion
    opc=libreria.pedir_entero("Ingrese Opciones:",1,3)

    #3. Mapeo de la opcion
    if(opc == 1):
        opcionA()
    if(opc == 2):
        opcionB()
    #fin mapeo


#fin_while
print("Fin del MENU")
