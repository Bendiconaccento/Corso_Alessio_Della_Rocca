# Scrivete un programma che riceve in input una
# stringa lunga e verifica se ci sono duplicati, 
# quanti sono, quali sono e
# quanto sono lunghi i duplicati.

def trova_duplicati(stringa):

    # Dizionario per contare la frequenza di ogni sottostringa
    # le chiavi saranno i duplicati e i valori le occorrenze
    duplicati = {}

    #lunghezza stringa
    n = len(stringa)

    for lunghezza in range(2, n):   #le sottostringhe devono essere almeno di lunghezza 2 fino a n-1

        for i in range(n - lunghezza + 1):
            sottostringa = stringa[i:i + lunghezza]
            # Aggiungiamo la sottostringa al dizionario e contiamo le occorrenze
            if sottostringa in duplicati:
                duplicati[sottostringa] += 1
            else:
                duplicati[sottostringa] = 1
    
    # Filtra le sottostringhe che sono presenti più di una volta
    duplicati_filtrati = {k: v for k, v in duplicati.items() if v > 1}
    
    # Verifica se ci sono duplicati
    if not duplicati_filtrati:
        print("Non ci sono duplicati nella stringa.")
    else:
        print(f"Sono stati trovati {len(duplicati_filtrati)} duplicati.")
        for sottostringa, occorrenze in duplicati_filtrati.items():
            print(f"Sottostringa: '{sottostringa}' | Lunghezza: {len(sottostringa)} | Occorrenze: {occorrenze}")

# Esempio di utilizzo:
stringa = input("Inserisci una stringa: ")
trova_duplicati(stringa)



