
class Libro:
    def __int__(self, titolo, autore, pagine):
        self.titolo = titolo
        self.autore = autore
        self.pagine = pagine

    def descrizione(self):                          # Restituisce la descrizione del libro

        return f"Il libro {self.titolo} è stato scritto da {self.autore} e ha {self.pagine} pagine."