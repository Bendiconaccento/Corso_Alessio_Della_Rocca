
# Scrivete un programma che utilizza il cifrario di Cesare per criptare una
# parola o decriptarla.
# Il Cifrario di Cesare è un algoritmo di crittografia che consiste nello spostare
# ciascuna lettera di una certa quantità di posti nell'alfabeto. Per utilizzarlo, si
# sceglie una chiave (scelta dall’utente) che rappresenta il numero di posti
# di cui ogni lettera dell'alfabeto verrà spostata: ad esempio, se si sceglie
# una chiave di 3, la lettera A diventerà D, la lettera B diventerà E e così via.
# Per decifrare un messaggio cifrato con il cifrario di Cesare bisogna
# conoscere la chiave utilizzata e spostare ogni lettera indietro di un numero
# di posti corrispondente alla chiave.


def cifra (testo, chiave):
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    risultato = ""

    for char in testo: 
        if char in alfabeto:
            #Trova l'indice (posizione) del carattere char nell'alfabeto
            indice = alfabeto.index(char)
            #Garantisce che l'indice rimanga all'interno dell'intervallo dell'alfabeto (0-25), permettendo così la rotazione ciclica
            nuovo_indice = (indice + chiave) % 26 
            #Aggiunge il carattere criptato (basato sul nuovo indice) alla variabile risultato 
            risultato += alfabeto[nuovo_indice]
        
        else:
            risultato += char
    #Restituisce la stringa criptata finale.
    return risultato


def decifra(testo, chiave):
    return cifra(testo, -chiave)


def utente():

    scelta = input("Vuoi criptare o decriptare? (C/D): ").lower()
    messaggio = input("Inserisci il messaggio: ").lower()
    chiave = int(input("Inserisci la chiave (numero intero): "))

    if scelta == "c":
        criptato = cifra(messaggio, chiave)
        print(f"Il messaggio criptato è:{criptato} ")
    
    elif scelta == "d":
        decriptato = decifra(messaggio, chiave)
        print(f"Il messaggio decriptato è:{decriptato} ")
    
    else:
        print("Scelta non valida")


utente()