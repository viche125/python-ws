# ---------------------------
# Fundamentos de Python
# ---------------------------

# Variables y tipos de datos
nombre = "Jazmin"
tipo = type(nombre)
print("El tipo de dato es: ", tipo)
edad = 30
tipo = type(edad)
print(f"El tipo de dato es: {tipo}")
edad = False
tipo = type(edad)
print(f"El tipo de dato es: {tipo}")
altura = 1.65
esEstudiante = True
variableUsada = "si si esta usada"
print(nombre, edad, altura, es_estudiante)
print(type(nombre), type(edad), type(altura), type(es_estudiante))

# Operadores básicos
a = 10
b = 3
print('Suma:', a + b)
print('Resta:', a - b)
print('Multiplicación:', a * b)
print('División:', a / b)
print('Módulo:', a % b)
print('Potencia:', a ** b)

# ---------------------------
# Estructuras de control
# ---------------------------

# Condicionales
numero = 7
if numero > 0:
    print("Es positivo")
elif numero < 0:
    print("Es negativo")
else:
    print("Es cero")

# Comparaciones
x = 15
y = 20
print(x == y)  # False
print(x != y)  # True
print(x < y)   # True

# Booleanos
llueve = True
tengo_paraguas = False

if llueve and tengo_paraguas:
    print("Puedo salir tranquilo")
elif llueve and not tengo_paraguas:
    print("Me voy a mojar")
else:
    print("Día soleado")

# ---------------------------
# Bucles
# ---------------------------

# Bucle for
for i in range(5):
    print("Número:", i)

# Bucle while
contador = 0
while contador < 5:
    print("Contador:", contador)
    contador += 1

# ---------------------------
# Funciones
# ---------------------------

def saludar(nombre):
    return f"Hola, {nombre}!"

print(saludar("Alison"))

def suma(x, y):
    return x + y

print("Suma:", suma(3, 4))

# ---------------------------
# Manejo de errores
# ---------------------------

try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("No se puede dividir por cero")
finally:
    print("Fin del bloque try-except")


