#Proyecto 1 Joaquin Andres Luis Fernando  
#Calculadora I.M.C
# Función para pedir un dato que no esté vacío
def ingrese_dato(mensaje):
    dato = input(mensaje)
    while not dato:  # Mientras el dato esté vacío
        print("¡Este campo no puede estar vacío!")
        dato = input(mensaje)
    return dato

# Función para pedir un número válido (edad, peso, estatura)
def pedir_numero(mensaje):
    while True:
        try:
            dato = float(input(mensaje))  # Intentamos convertirlo a número
            if dato <= 0:
                print("El número debe ser mayor que cero.")
            else:
                return dato
        except ValueError:  # Si no es un número válido
            print("Por favor ingresa un número válido.")

# Función para calcular el IMC y clasificarlo
def calcular_imc(peso, estatura):
    imc = peso / (estatura ** 2)  # Fórmula del IMC
    if imc < 18.5:
        clasificacion = "Peso bajo, acuda al medio"
    elif 18.5 <= imc < 25:
        clasificacion = "Peso normal, excelente por ti"
    elif 25 <= imc < 30:
        clasificacion = "Sobrepeso, cuida mas tu salud"
    elif 30 <= imc < 35:
        clasificacion = "Obesidad leve, acude al medico"
    elif 35 <= imc < 40:
        clasificacion = "Obesidad media, acude al medio de inmediato"
    else:
        clasificacion = "Obesidad mórbida, solicita apoyo prfesional"
    return imc, clasificacion

# Pedir al usuario los datos requeridos
nombre = ingrese_dato("¿Cuál es tu nombre? ")
apellido_paterno = ingrese_dato("¿Cuál es tu apellido paterno? ")
apellido_materno = ingrese_dato("¿Cuál es tu apellido materno? ")
edad = pedir_numero("¿Cuántos años tienes? ")
peso = pedir_numero("¿Cuánto pesas en kg? ")
estatura = pedir_numero("¿Cuál es tu estatura en metros? ")

# Calcular el IMC y clasificarlo
imc, clasificacion = calcular_imc(peso, estatura)

# Mostrar los resultados
print("\nResumen de los datos ingresados:")
print(f"Nombre: {nombre} {apellido_paterno} {apellido_materno}")
print(f"Edad: {edad} años")
print(f"Peso: {peso} kg")
print(f"Estatura: {estatura} metros")
print(f"Índice de Masa Corporal (IMC): {imc:.2f}")
print(f"Clasificación: {clasificacion}")
