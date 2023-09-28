#Cadena de Texto en Python

str = "Hola Mundo" #Variable str

print(f"Hola {str}") #imprime variable str junto el texto

#dir(str) - Muestra el uso de cualquier elemento

#Metodos

print(str.upper()) #Metodo Mayuscula
print(str.lower()) #Metodo Miniscula
print(str.swapcase()) #Metodo a 1 letra de cada frase a Miniscula
print(str.capitalize()) #Metodo a 1 letra de cada frase a Mayuscula
print(str.replace("Hola", "Hello")) #Metodo reemplazar las frases
print(str.replace("Hello", "Hola").upper()) #Metodo Con Otro Metodo
print(str.count("H")) #Metodo Analiza las palabras de la variable
print(str.startswith("Hola")) #Metodo Analiza las palabras existentes al inicio
print(str.endswith("Mundo")) #Metodo Analiza las palabras existentes al final
print(str.split("-")) #Metodo separa las palabras del string
print(str.find("5")) #Metodo analiza la posicion del string
print(len(str)) #Metodo analiza las palabras del string
print(str.index("l")) #Metodo analiza las letras de la frase del string
print(str.isnumeric()) #Metodo analiza las frases si es numerica
print(str.isalpha()) #Metodo analiza las frase si es texto
print(str[2]) #Metodo analiza el texto con la posiones en letra