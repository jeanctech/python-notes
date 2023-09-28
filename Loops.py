#Bucles en Python

#Ciclos For

comida = ["queso", "maracuya", "tomate"]

for comida in comida:
    print(comida)
    break

for comida in comida:
    if comida == "queso":
        print("correcto")
        break
    print(comida)

for comida in comida:
    if comida == "queso":
        print("correcto")
        continue
    print(comida)

for numeros in range(1, 8):
    print(numeros)

for letras in ("Hola Mundo:"):
    print(letras)

#Ciclos While

#1
contar = 4

while contar <= 2:
    print(contar)
    contar = contar + 1

#2
suma = 1+1

while suma <=2:
    print(suma)
    suma = contar + 1