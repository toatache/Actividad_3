while True:
    num = int(input("Ingrese un numero: "))
    i = 1
    if  num < 0:
        print("Solo positivos")
    else:
        while True:
            print(i ** 2)
            i += 1
            if i > num:
                break
        print("Secuencia de cuadrados hasta el ", num)

    # mensaje de continuar 
    print("Otro numero? ")
    res = input("(si) = s/(no) = otra tecla: ").lower()
    if res == "s":
        print("Continuemos")
    else:
        break
print("ADIOS")