#Base / Numeri pari e dispari o sequenza

while True:

    #.strip() elimina spazi vuoti
    scelta = input("Vuoi inserire un numero o una stringa? (numero/stringa): ").strip().lower()

    if scelta == "numero":
        numero = input("Inserire numero: ")

        #converti la stringa in un intero per poter fare le operazioni
        numero = int(numero)

        if numero % 2 == 0:
           print(f"{numero} è pari")
        
        else:
            print(f"{numero} è dispari")


    elif scelta == "stringa":
       stringa = input("Inserisci una stringa: ")
       print(f"Hai inserito una stringa: {stringa}")

    else:
        print("Scelta non valida")


    ripetere = input("Vuoi ripetere? (si/no): ")
    if ripetere != "si":
        break




    
    

