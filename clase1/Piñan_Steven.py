# tu_nombre_tu_apellido.py

def calcular_imc(peso, talla):
    """Calcula el IMC dado peso (kg) y talla (m)."""
    return peso / (talla ** 2)

def clasificar_imc(imc):
    """Devuelve la categoría según el valor de IMC."""
    if imc < 18.5:
        return "Bajo peso"
    elif imc < 25.0:
        return "Peso saludable"
    elif imc < 30.0:
        return "Sobrepeso"
    else:
        return "Obesidad"

def main():
    # 1. Solicitar datos al usuario
    nombre = input("Nombre: ")
    edad   = input("Edad: ")
    talla  = float(input("Talla (m): "))
    peso   = float(input("Peso (kg): "))

    # 2. Calcular IMC
    imc = calcular_imc(peso, talla)

    # 3. Mostrar resultado
    print(f"\nHola {nombre}, tu IMC es {imc:.2f}.")
    print(f"Tienes {clasificar_imc(imc)}.")

if __name__ == "__main__":
    main()
