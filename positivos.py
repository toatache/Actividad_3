suma = 0
cont = 0
while True:
    num = float(input("Numero positivo(negativo = salir): "))
    if num < 0:
        break
    if num > 0:
        suma += num
        cont += 1
if cont > 0:
    media = suma / cont
    print("La media es:", media)
else:
    print("No se registro ningun numero porsitivo")