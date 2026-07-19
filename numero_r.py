import random
while True:
    secreto = random.randint(1, 100)
    while True:
        inten = int(input("Adivina el numero del 1 al 100(espacio salir): "))
        if inten < secreto:
            print("Demasiado bajo")
        elif inten > secreto:
            print("Demasiado alto")
        else:
            print("Acertaste es ", secreto)
            break
    
    # mensaje de continuar 
    print("Volver a jugar? ")
    res = input("(si) = s/(no) = otra tecla: ").lower()
    if res == "s":
        print("Continuemos")
    else:
        break
print("ADIOS")