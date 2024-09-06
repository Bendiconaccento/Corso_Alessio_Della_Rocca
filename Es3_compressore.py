
# Disclaimer: avevo l'idea del conteggio ma se non avessi visto il tuo codice (Mirko) ci avrei messo una vita

# Il decoratore mostra messaggi prima e dopo la compressione della stringa
def dec_compressione(funzione):
    def wrapper(s):
        print("Compressione in corso...")
        risultato = funzione(s)
        print(f"Compressione competata, il risultato è: {risultato}")
        return risultato
    return wrapper


@dec_compressione

# Restituisce la stringa compressa se la lunghezza è minore della stringa stessa
def comprimi_stringa(s):

    # Se la stringa è vuota restituisce una stringa vuota
    if not s:
        return ""
    
    compressa = []
    conteggio = 1

    # L'iterazione parte dal secondo carattere (1) così possiamo confrontarlo con quello precedente
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            conteggio += 1

        # Scrive nella lista il carattere precedente e il conteggio che poi si riavvia    
        else:
            compressa.append(s[i - 1] + str(conteggio))
            conteggio = 1
    
    # Il ciclo for non aggiunge l'ultimo carattere perché alla fine della stringa non c'è un carattere diverso dal precedente
    # quindi lo si fa esplicitamente - riga di codice che non mi sarebbe venuta in mente -
    compressa.append(s[-1] + str(conteggio))

    # join= prende una lista di stringhe e le unisce in una singola
    stringa_compressa = "".join(compressa)

    # restituisce la stringa compressata se la lunghezza è minore di quella originale, sennò restituisce l'originale
    return stringa_compressa if len(stringa_compressa) < len(s) else s


stringa_prova = input("Inserisci la stringa da comprimere: ")
risultato = comprimi_stringa(stringa_prova)
print("Risultato: ", risultato)
