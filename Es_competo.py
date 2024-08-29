while True:
 numero= int(input("Iserisci numero: "))

 if numero % 2 == 0:        # funzione presa da Chat: (resto della divisione) 
    print("Pari")

 else:
    print("Dispari")

 ripetere = input("Vuoi ripetere? (si/no): ")
 if ripetere != "si":
    print("Fine")
    break


while True:
    numero = int(input("Inserisci un numero intero positivo: "))
    if numero < 0:
        print("Il numero deve essere positivo")

    for i in range(numero, -1, -1):
        print(i)
    
    ripetere = input("Vuoi ripetere? (si/no): ")
    if ripetere != "si":
        print("Fine")
        break