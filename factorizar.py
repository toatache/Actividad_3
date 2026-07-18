while True:
    num = int(input("Numero a factorizar: "))
    factorial = 1
    if  num < 0:
        print("No es posible factorizar negativos")
    else:
        for i in range(1, num + 1):
            factorial *= i
        print("El factorial de", num, "es: ", factorial) 

    # mensaje de continuar 
    print("Factorizar otro? ")
    res = input("(si) = s/(no) = otra tecla: ").lower()
    if res == "s":
        print("Continuemos")
    else:
        break
print("ADIOS")