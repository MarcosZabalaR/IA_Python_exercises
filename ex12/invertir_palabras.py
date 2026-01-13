def invertir_cadena(cadena):
    return cadena[::-1]
palabra = input("Ingrese una palabra: ")
palabra_invertida = invertir_cadena(palabra)
print(f"La palabra invertida es: {palabra_invertida}")
