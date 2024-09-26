
from ristorante import Ristorante

def utente():
    nome = input("Inserisci il nome del ristorante: ")
    tipo_cucina = input("Inserisci tipo di cucina: ")

    ristorante = Ristorante(nome, tipo_cucina)

    apertura = input("Vuoi aprire il ristorante? (s/n): ")

    if apertura.lower() == "s":
        ristorante.apri_ristorante()

    while True:

        piatto = input("Inserisci nome del piatto (oppure 'fine' per terminare): ")

        if piatto.lower() == "fine":
            break
    
        else:
            prezzo = float(input(f"Inserisci prezzo di {piatto}: "))
            ristorante.aggiungi_al_menu(piatto, prezzo)
    
    ristorante.stampa_menu()

    chiusura = input("Vuoi chiudere il ristorante? (s/n): ")

    if chiusura.lower() == "s":
        ristorante.chiudi_ristorante()

utente()