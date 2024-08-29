
numero = int(input("Inserisci un numero: "))
X=True
while X:
    print(numero)
    for num in range(numero, -1, -1):
        print(num)

    ripetere = input("Vuoi ripetere? (si/no): ")

    if ripetere != "si":
       print("Fine")
       X=False