while True:
    num1 = int(input("Ingrese desde que numero emmpezara la secuencia: "))
    suma = int(input("La diferencia: "))
    limi = int(input("El limite de la secuencia: "))
    ini = num1
    if  limi > num1:
        while  True:
            print(num1, end="-")
            num1 += suma
            if num1 > limi:
                break
        print("\nSecuencia finalizada del ", ini, "--", limi)
    else:
        print("El limite debe ser mayor que el numeor inicial")

    # mensaje de continuar 
    print("Verificar otro? ")
    res = input("s/otra tecla: ").lower()
    if res == "s":
        print("Continuemos")
    else:
        break
print("ADIOS")