
class Libro:

    def __init__ (self, titolo, autore, pagine):    # Inizializza i tre attributi

        self.titolo = titolo
        self.autore = autore
        self.pagine = pagine

    def descrizione(self):                          # Restituisce la descrizione del libro

        return f"Il libro {self.titolo} è stato scritto da {self.autore} e ha {self.pagine} pagine."
    
libro = Libro("Il Gattopardo", "Tomasi Di Lampedusa", 299)
print(libro.descrizione())                          # Printa la descrizione del libro