while True:
    n = int(input("Ingresar el numero positivo: "))
    i = 0
    while True:
        if i % 2 != 0:
            print(i, end="--")
        i += 1
        if i > n:
            break
    print("\nFin del programa")

    # mensaje de continuar 
    print("Ingresar otro numero? ")
    res = input("(si) = s/(no) = otra tecla: ").lower()
    if res == "s":
        print("Continuemos")
    else:
        break
print("ADIOS")