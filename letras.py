while True:
    letra = input("Ingresar letra(espacio salir): ")
    if letra in "1234567890":
        print("No es una letra")
    else:
        if letra == " ":
            break
        letra = letra.lower()
        if letra in "aeiou":
            print("Vocal")
        else:
            print("Consonante")
print("Programa finalizado")