def stampa_quadrati():
    # Chiedi all'utente di inserire una lista di numeri separati da uno spazio
    input_numeri = input("Inserisci una lista di numeri separati da uno spazio: ")
    
    # Dividi l'input in una lista di stringhe, poi convertili in numeri interi
    lista_numeri = [int(x) for x in input_numeri.split()]
    
    # Ciclo for per calcolare e stampare il quadrato di ciascun numero
    for numero in lista_numeri:
        quadrato = numero ** 2
        print(f"Il quadrato di {numero} è {quadrato}")

# Esegui la funzione stampa_quadrati
stampa_quadrati()