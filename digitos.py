while True:
    num = int(input("Ingrese un numero: "))
    if  num == 0:
        digitos = 1
    else:
        digitos = 0
        if num < 0:
            num = abs(num)
        while num > 0:
            num //= 10
            digitos += 1
    print("Tiene:", digitos, " digitos")

    # mensaje de continuar 
    print("Otro numero? ")
    res = input("(si) = s/(no) = otra tecla: ").lower()
    if res == "s":
        print("Continuemos")
    else:
        break
print("ADIOS")