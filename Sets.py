#Conjuntos en Python

colores = {"azul", "verde", "amarillo"} #Tipo de Sets

print(type(colores)) #Imprime el tipo de la variable colores

print(colores) #imprime la variable colores

print("azul" in colores) #Muestra si azul esta en el sets
print("rojo" in colores) #Muestra si rojo esta en el sets

colores.add("rojo")
print(colores)

colores.remove("rojo")
print(colores)

colores.clear()
print(colores)

# del colores
# print(colores)