def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
num = int(input("Ingrese un número entero no negativo: "))
if num < 0:
    print("El número debe ser no negativo.")
else:
    resultado = factorial(num)
    print(f"El factorial de {num} es {resultado}")
    