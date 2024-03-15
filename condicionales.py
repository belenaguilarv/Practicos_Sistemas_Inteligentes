# Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.

edad = input("Cual es tu edad? ")

while not edad.isdigit() or int(edad) <= 0:
    edad = input("Anota un valor válido. Cual es tu edad? ")

edad = int(edad)

if edad > 17: 
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")

'''

En una determinada empresa, sus empleados son evaluados al final de cada año. Los puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir aumentando, traduciéndose en mejores beneficios. Los puntos que pueden conseguir los empleados pueden ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre las cifras mencionadas. A continuación se muestra una tabla con los niveles correspondientes a cada puntuación. La cantidad de dinero conseguida en cada nivel es de 2.400€ multiplicada por la puntuación del nivel.

Nivel	Puntuación
Inaceptable	0.0
Aceptable	0.4
Meritorio	0.6 o más

Escribir un programa que lea la puntuación del usuario e indique su nivel de rendimiento, así como la cantidad de dinero que recibirá el usuario.

'''

dinero = 2400
puntuacion = float(input("Ingrese la puntuación que obtuvo el empleado: "))
    
if puntuacion == 0.0 :
    nivel = "Inaceptable"
    print("Nivel de rendimiento ", nivel, "No goza de beneficios")
elif puntuacion == 0.4 :
    nivel = "Aceptable"
    premio = dinero * puntuacion
    print("Nivel de rendimiento ", nivel, ". La cantidad de dinero que recibirá es de ", premio, "$")
elif puntuacion >= 0.6: 
    nivel = "Meritorio"
    premio = dinero * puntuacion
    print("Nivel de rendimiento ", nivel, ". La cantidad de dinero que recibirá es de ", premio, "$")
else: 
    print("Puntuación no válida. La puntuación debe ser 0.0, 0.4 o mayor que 0.6")



# Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar 5€ y si es mayor de 18 años, 10€.

edad = int(input("Ingrese la edad del cliente: "))

if edad < 4:
    print("Puede ingresar gratis.")
elif edad > 3 and edad < 19:
    print("Debe pagar 5$.")
else:
    print("Debe pagar 10$.")

# La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.
# Ingredientes vegetarianos: Pimiento y tofu. Ingredientes no vegetarianos: Peperoni, Jamón y Salmón. Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.

print("Bienvenido a la pizzería Bella Napoli! ¿Qué tipo de pizza te gustaría ordenar?")
print("1. Pizza vegetariana")
print("2. Pizza no vegetariana")

option = int(input("Ingrese el número correspondiente a su elección: "))

if option == 1:
    print("Genial!.Todas las pizzas ya vienen con mozzarella y tomate, puede agregar uno de los ingredientes extra a su pizza vegetariana: ")
    print("1. Pimiento")
    print("2. Tofu")
    extra = int(input("Seleccione el número correspondiente al ingrediente que desea añadir a su pizza: "))
    if extra == 1:
        print("Excelente! Los ingredientes de su pizza vegetariana son: mozzarella, tomate y pimiento")
    elif extra == 2:
        print("Excelente! Los ingredientes de su pizza vegetariana son: mozzarella, tomate y tofu")
elif option == 2:
    print("Genial!.Todas las pizzas ya vienen con mozzarella y tomate, puede agregar uno de los ingredientes extra a su pizza no vegetariana: ")
    print("1. Peperoni")
    print("2. Jamón")
    print("3. Salmón")
    extra = int(input("Seleccione el número correspondiente al ingrediente que desea añadir a su pizza: "))
    if extra == 1:
        print("Excelente! Los ingredientes de su pizza no vegetariana son: mozzarella, tomate y peperoni")
    elif extra == 2:
        print("Excelente! Los ingredientes de su pizza no vegetariana son: mozzarella, tomate y jamón")
    elif extra == 3:
        print("Excelente! Los ingredientes de su pizza no vegetariana son: mozzarella, tomate y salmón")
