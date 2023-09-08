#Listas en Python

texto = ["uno", "uno", "dos"] #Lista de Texto

interger = [1, 2, 3] #Lista de interger

float = [1,0, 2,0, 3,0] #Lista de float

bool = [True, False, True] #Lista de Boolean

lis = list ((1.1, 2.2, 3.3)) #lista de lista

print(lis) #Imprime la lista con la variable lis

rango = list(range(1, 11)) #lista con un inicio y fin

print(rango) #Imprime la lista de la variable un

print(len(lis)) #len analiza los numeros de la lista

# print(dir(lis)) #dir analiza el uso del metodo

print(type(lis)) #Analiza el tipo de metodo

print(lis[1]) #imprime la posicion de la lista

print(lis[-1]) #imprime la posicion de la lista inversa

print("uno" in texto) #analiza las palabras de una lista

texto [0] = "cero" #Cambia elemento de una lista

print(texto)

# texto.append("tres") #agrega un elemento de una lista

texto.extend(["tres", "cuatro"]) #agrega mas de un elemento en una lista
print(texto)

texto.insert(5, "cinco") #insertar posicion y texto en una lista

texto.pop() #Elimina el ultimo elementos de una lista
print(texto) #Imprime la lista texto


texto.pop(1) #Elimina el ultimo elementos de una lista
print(texto) #Imprime la lista texto


texto.remove("tres") #Eliminar todos los elementos de una lista
print(texto) #Imprime los elementos de la lista

texto.sort() #Ordena alfabenticamente la lista
print(texto) #imprime la lista

texto.sort(reverse=True) #Ordena alfabenticamente de reversa la lista
print(texto) #imprime la lista

print(texto.index('dos')) #analiza el index de la lista

print(texto.count('dos')) #cuenta el index de la lista