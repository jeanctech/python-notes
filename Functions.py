#Funciones en Python

# print()
# dir()
# type()

def hola():
    print("Hola Mundo")

hola()

name = "neo"

def hola(name):
    print("Hola " + name)

hola("neo")

#Funcion def

def suma(uno, dos):
    return uno + dos

print(suma(10, 20))

print(suma(20, 10))

#Funcion Lambda

suma = lambda uno, dos: uno + dos

print(suma(20, 20))
