# Escribir un programa que muestre por pantalla la cadena ¡Hola Mundo!.
print("¡Hola Mundo!")

#Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla la cadena ¡Hola !, donde es el nombre que el usuario haya introducido.

nombre = input("Cual es su nombre? ")
print("Hola", nombre + "!")

#Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.

worked_hours = float(input("Ingrese la cantidad de horas trabajadas: "))
cost_per_hour = float(input("Ingrese el costo por hora: "))
salary = worked_hours * cost_per_hour
print("La paga que le corresponde por las", worked_hours, "horas trabajadas es", salary, "$")

#Escribir un programa que lea un entero positivo, n, introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta n. La suma de los n primeros enteros positivos puede ser calculada de la siguiente forma: suma = (n(n+1))/2
n = None

while n is None or n <= 0:
    try:
        n = int(input("Ingrese un número positivo: "))
        if n <= 0:
            print("El número debe ser positivo. Ingrese nuevamente.")
    except ValueError:
        print("Ingrese un número válido.")

suma = (n * (n + 1)) / 2
print("La suma de los enteros desde 1 hasta", n, "es:", suma)

#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión.

inversion = float(input("Cuanto dinero desea invertir? "))
interes_anual = float(input("A que tasa de interés anual? "))
anios = int(input("A cuantos años? "))

capital = inversion * (1 + interes_anual / 100) ** anios 
capital = round(capital,2)

print("El capital obtenido en la inversión después de", anios, "años es:", capital, "$")
