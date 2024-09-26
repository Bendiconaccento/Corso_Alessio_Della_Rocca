'''Scrivete un programma che chiede una stringa all’utente e
restituisce un dizionario rappresentante la "frequenza di
comparsa" di ciascun carattere componente la stringa.
Esempio:
Stringa "ababcc",
Risultato
{"a": 2, "b": 2, "c": 2}'''


frequenza = {}

stringa = input("Inserisci una stringa: ")

# se il carattere non è presente, restituisce 0. Poi aggiunge 1 per aggiornare la frequenza
for carattere in stringa:
     frequenza[carattere] = frequenza.get(carattere, 0) + 1

print(f"Frequenza di comparsa dei caratteri: {frequenza}")


