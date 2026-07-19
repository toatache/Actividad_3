while True:
    pal = input("Ingrese la palabra a analizar: ").lower()
    cont = 0
    for letra in pal:
        if letra == 'a':
            cont += 1
    print("Hay un total de ", cont, "letras 'a'")

    # mensaje de continuar 
    print("Utilizar otra palabra? ")
    res = input("(si) = s/(no) = otra tecla: ").lower()
    if res == "s":
        print("Continuemos")
    else:
        break
print("ADIOS")