import libreria
#1
assert(libreria.validar_coontinente("asia")==True)
assert(libreria.validar_continente("america")==True)
assert(libreria.validar_continente("a")==False)
assert(libreria.validar_continente("africa")==False)
print("validar continente  -------> OK")

#2
assert libreria.validar_entero("a") == False
assert libreria.validar_entero("20") == False
assert libreria.validar_entero(10) == True
assert libreria.validar_entero(-2) == True
print("validar_entero OK")

#3
assert libreria.validar_rango("hola",12,"adios") == False
assert libreria.validar_rango(-2,12,"adios") == False
assert libreria.validar_rango(4,0,8) == True
assert libreria.validar_rango(6,6,6) == True
print("validar_rango OK")

#4
assert(libreria.validar_año("a")==False)
assert(libreria.validar_año("200")==True)
assert(libreria.validar_año("123")==False)
assert(libreria.validar_año("20.30")==False)
print("validar continente  -------> OK")


#5
assert(libreria.validar_sexo("masculino")==True)
assert(libreria.validar_sexo("femenino")==True)
assert(libreria.validar_sexo("acf")==False)
assert(libreria.validar_sexo("mujer")==False)
print("validar continente  -------> OK")


#6
assert(libreria.validar_coontinent("asia")==True)
assert(libreria.validar_continente("america")==True)
assert(libreria.validar_continente("a")==False)
assert(libreria.validar_continente("africa")==False)
print("validar continente  -------> OK")


#7
assert(libreria.validar_carrera("medicina")==True)
assert(libreria.validar_carrera("arquitectura")==True)
assert(libreria.validar_carrera("a")==False)
assert(libreria.validar_carrera("chofer")==False)
print("validar continente  -------> OK")

#8
assert(libreria.validar_frutas("fresa")==True)
assert(libreria.validar_frutas("pera")==True)
assert(libreria.validar_frutas("a")==False)
assert(libreria.validar_frutas("2123")==False)
print("validar continente  -------> OK")















