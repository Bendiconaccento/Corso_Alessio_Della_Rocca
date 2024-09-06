import random

# Funzione per randomizzare presa da Brave (browser di ricerca con IA integrata)
def indovina_numero():
    numero_random = random.randint(1,100)
    print("Benvenuto nel gioco!")
    print("Indovina un numero tra 1 e 100")
    print("Digita 'exit' se vuoi uscire dal gioco")
    
    while True:

        scelta = input("inserisci il tuo numero o digita exit: ")

        if scelta.lower() == "exit":
            print(f"Il numero era: {numero_random}. Grazie, arrivederci!")
            break

        scelta = int(scelta)

        if scelta < 1 or scelta > 100:
            print("Il numero deve essere compreso tra 1 e 100. Riprova.")
            continue
    
        if scelta < numero_random:
            print("Il numero è più alto")

        elif scelta > numero_random:
            print("Il numero è più basso")
        
        else:
            print(f"Il numero è corretto! Il numero era {numero_random}")

            break
    
indovina_numero()





