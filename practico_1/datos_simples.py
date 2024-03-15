
# Escribir un programa que muestre por pantalla la cadena ¡Hola Mundo!.
print("¡Hola Mundo!")

# Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla la cadena ¡Hola !, donde es el nombre que el usuario haya introducido.

nombre = input("Cual es su nombre? ")
print("Hola", nombre + "!")

# Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.

worked_hours = float(input("Ingrese la cantidad de horas trabajadas: "))
cost_per_hour = float(input("Ingrese el costo por hora: "))
salary = worked_hours * cost_per_hour
print("La paga que le corresponde por las", worked_hours, "horas trabajadas es", salary, "$")

# Escribir un programa que lea un entero positivo, n, introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta n. La suma de los n primeros enteros positivos puede ser calculada de la siguiente forma: suma = (n(n+1))/2
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

# Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión.

inversion = float(input("Cuanto dinero desea invertir? "))
interes_anual = float(input("A que tasa de interés anual? "))
anios = int(input("A cuantos años? "))

capital = inversion * (1 + interes_anual / 100) ** anios 
capital = round(capital,2)

print("El capital obtenido en la inversión después de", anios, "años es:", capital, "$")

# Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado.
weight_clown = 112
weight_doll = 75

def calcular_peso_total(num, peso_unit):
    peso_total = num * peso_unit
    if peso_total > 1000:
        peso_total /= 1000
        unidad = "kg"
    else:
        unidad = "g"
    return peso_total, unidad

num_clown = int(input("¿Cuántos payasos vendió? "))
num_doll = int(input("¿Cuántas muñecas vendió? "))

total_clown, unidad_clown = calcular_peso_total(num_clown, weight_clown)
total_doll, unidad_doll = calcular_peso_total(num_doll, weight_doll)

print("El peso total de los", num_clown, "payasos es:", total_clown, unidad_clown)
print("El peso total de las", num_doll, "muñecas es:", total_doll, unidad_doll)

# Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta de ahorros. Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida por el usuario. Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada cantidad a dos decimales.

interes = 0.04

dinero_cuenta = float(input("Cuanto dinero tiene depositado en su cuenta? "))

ahorro_anio_uno = round(dinero_cuenta * (1 + interes), 2)
ahorro_anio_dos = round(ahorro_anio_uno * (1 + interes),2)
ahorro_anio_tres = round(ahorro_anio_dos * (1 + interes),2)

print("Los ahorros que tendrá despues del primer año son: ", ahorro_anio_uno, " $")
print("Los ahorros que tendrá despues del segundo año son: ", ahorro_anio_dos, " $")
print("Los ahorros que tendrá despues del tercer año son: ", ahorro_anio_tres, " $")

# Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. Escribir un programa que comience leyendo el número de barras vendidas que no son del día. Después el programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca y el coste final total.

bread = 3.49
discount = 0.6

sold_bread = int(input("Cuantas barras de pan que no son del día vendió? "))

unit_price = bread * (1- discount)

total = round(sold_bread * unit_price, 2)

print("Bueno, el precio habitual del pan es ", bread, "$. Le haremos un descuento del 60%, así que le queda en ", total, "$.")


