
while True:
        scelta = input("Vuoi inserire un numero o una stringa? (numero/stringa): ").strip().lower()
        
        if scelta == "numero":
            numero = input("Inserisci un numero: ")
            try:
                numero = int(numero)
                if numero % 2 == 0:
                    print(f"{numero} è pari.")
                else:
                    print(f"{numero} è dispari.")
            except ValueError:
                print("Non hai inserito un numero valido.")
        
        elif scelta == "stringa":
            stringa = input("Inserisci una stringa: ")
            print(f"Hai inserito la stringa: {stringa}")
        
        else:
            print("Scelta non valida.")
            continue
        
        ripetere = input
