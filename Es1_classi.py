import math


class Punto:

    def __init__(self, x = 0, y = 0): # metodo costruttore
        self.x = x                    #attributo di istanza
        self.y = y                    #attributo di istanza
    
    def muovi(self, dx, dy):          # metodo di istanza
        self.x += dx                  # aggiunge all'attributo x il valore dx
        self.y += dy                  # aggiunge all'attributo y il valore dy

    def distanza_da_origine(self):    # metodo che calcola la distanza dal punto di origine (0,0)

        return math.sqrt(self.x**2 + self.y**2)    # formula presa da Chat


p = Punto(7, 8)     # coordinate di un Punto
print("Distanza dall'origine: ", p.distanza_da_origine())       # Printa la distanza dall'origine


p.muovi(2, -3)      # sposta il punto di dx = 2, dy = -3
print("Nuova distanza dall'origine: ", p.distanza_da_origine())