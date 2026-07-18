while True:
    opc = int(input("~~MENU~~ || 1.Suma 2.Resta 3.Multi 4.Division 5.Salir\nOpcion: "))
    if  opc == 5:
        break
    a = float(input("Primer numero: "))
    b = float(input("Segundo numero: "))
    match opc:
        case 1:
            print(f"Resultado: {a + b}")
        case 2:
            print(f"Resultado: {a - b}")
        case 3:
            print(f"Resultado: {a * b}")
        case 4:
            if b != 0:
                print(f"Resultado: {a / b}")
            else:
                print("No es posible dividir entre 0")
        case _:
            print("No es una opcion")

    # mensaje de continuar 
    print("Verificar otro? ")
    res = input("(si) = s/(no) = otra tecla: ").lower()
    if res == "s":
        print("Continuemos")
    else:
        break
print("ADIOS")