#Condiccionales en Python

#Condiccional mayor que

a = 20

if a > 18 :
    print("pase")
else :
    print("no pase")

#Condiccional menor que

b = 10

if b < 18 :
    print("pase")
else :
    print("no pase")

#Condicional igual que

c = 10

if c == 10 :
    print("pase")
else :
    print("no pase")

#Condiccional elif

texto = "uno"

if texto > "dos":
    print("es un uno")
elif texto > "dos":
    print("es cero")
else:
    print("no es un uno")

#Condiccional en cadena de texto

color = "rojo"

if color > "rojo":
    print("no es rojo")
else:
    print("si es rojo")

gol = "dos"

if gol > "uno":
    print("no es un gol")
else:
    print("si es gol")

#Condicionales Anidadas

nombre = "neo"
apellido = "xeo"

if nombre == "neo":
    if apellido == "xeo":
        print("Acceso Autorizado")
    else:
        print("Acceso no Autorizado")
else:
    print("Acesso Prohibido")

if color > "rojo":
    print("no es rojo")
else:
    print("si es rojo")

#Condicciones con Operadores Logicos

a = "10"
b = "20"

#Operador or

if a > "20" or a >= "40":
    print("no")
else:
    print("si")

#Operador and

if a < "20" and a <= "15":
    print("si")
else:
    print("no")
