# Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.

word = input("Ingrese una palabra: ")

for _ in range(10):
    print(word)

# Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.

for i in range (1,11):
    res = i * 10
    print(i, " x 10 = ", res)

# Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.

frase = input("Ingrese una frase: ")
letra = input("Ingrese una letra: ")
c = 0
for l in frase:
    if l == letra:    
        c += 1
print("La cantidad de veces que ", letra, " esta en ", frase, " es: ", c)

# Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.

ingreso = None

while ingreso != "salir": 
    ingreso = input("Inserte algo: ")
    print(ingreso)
