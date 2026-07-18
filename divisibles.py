print("Secuencia de los numeros divisibles por 3 y 5 entre el 1-100:")
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print(i, end="--")
print("")