while True:
    # Chiede all'utente di inserire due numeri per definire un intervallo
    start = input("Inserisci il primo numero dell'intervallo: ")
    end = input("Inserisci il secondo numero dell'intervallo: ")
    
    # Verifica che l'input sia costituito solo da cifre
    if start.isdigit() and end.isdigit():
        start = int(start)
        end = int(end)
        
        # Assicura che il primo numero sia minore o uguale al secondo
        if start > end:
            start, end = end, start
        
        # Liste per memorizzare numeri primi e non primi
        numeri_primi = []
        numeri_non_primi = []

        # Ciclo per controllare ogni numero nell'intervallo
        for numero in range(start, end + 1):
            # Verifica se il numero è primo
            if numero > 1:  # I numeri primi sono maggiori di 1
                primo = True
                for i in range(2, int(numero**0.5) + 1):
                    if numero % i == 0:
                        primo = False
                        break
                if primo:
                    numeri_primi.append(numero)
                else:
                    numeri_non_primi.append(numero)
            else:
                numeri_non_primi.append(numero)
        
        # Stampa i risultati
        print(f"Numeri primi tra {start} e {end}: {numeri_primi}")
        print(f"Numeri non primi tra {start} e {end}: {numeri_non_primi}")
    
    else:
        print("Hai inserito un numero non valido.")
        
    
    # Chiede all'utente se vuole ripetere l'operazione
    ripetere = input("Vuoi ripetere? (si/no): ").strip().lower()
    if ripetere != "si":
        break  # Esce dal ciclo e termina il programma
