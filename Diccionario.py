#Diccionario en Python

carrito = {
    "producto" : "book",
    "cantidad" : "20",
    "descripcion" : "book"
}

persona = {
    "usuario" : "neo",
    "apellido" : "rp",
    "cuenta" : "123",
}

print(type(persona))
print(type(carrito))

print(carrito.keys())
print(persona.keys())

print(carrito.items())
print(persona.items())

# del person - Elimina el diccionario

# persona.clear() - Limpia el diccionario

#diccionario en lista

compras = [
    {
    "producto" : "book",
    "cantidad" : "20",
    "descripcion" : "book",
    },
    {
    "producto" : "books",
    "cantidad" : "200",
    "descripcion" : "books",
    }
]
