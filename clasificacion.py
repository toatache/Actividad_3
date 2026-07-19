while True:
    n = int(input("Total de numeros a ingresar: "))
    may = 0
    men = 0
    igu = 0
    for i in range(n):
        num = int(input("Numero: "))
        if num > 0:
            may += 1
        elif num < 0:
            men += 1
        else:
            igu += 1
    print("Numeros Mayores a 0: ", may)
    print("Numeros Menores a 0: ", men)
    print("Numeros Iguales a 0: ", igu)

    # mensaje de continuar 
    print("Ingresar otros numeros? ")
    res = input("(si) = s/(no) = otra tecla: ").lower()
    if res == "s":
        print("Continuemos")
    else:
        break
print("ADIOS")