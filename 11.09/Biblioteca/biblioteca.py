
from libro import Libro

class Biblioteca:

    def __init__(self):
        self.libri = []
    
    def aggiungi_libro(self, titolo, autore, pagine):
        libro = Libro(titolo, autore, pagine)
        self.libri.append(libro)


    def stampa_libri(self):
        for libro in self.libri:
            libro.descrizione()
            print("-")


def utente():

    biblioteca = Biblioteca()

    while True:
        print("1. Aggiungi un libro")
        print("2. Visualizza tutti i libri")
        print("3. Esci")
        
        scelta = input("Scegli una opzione: ")

        if scelta == "1":
            titolo = input("Inserisci il titolo del libro: ")
            autore = input("Inserisci nome dell'autore: ")
            pagine = int(input("Inserisci il numero di pagine: "))
            
            biblioteca.aggiungi_libro(titolo, autore, pagine)
            print(f"Il libro {titolo} è stato aggiunto alla biblioteca")
        
        elif scelta == "2":
            biblioteca.stampa_libri()
        
        elif scelta == "3":
            print ("Uscita dal programma")
            break
        
        else:
            print("Scelta non valida")

utente()