
class Prodotto:

    def __init__(self, nome, costo_produzione, prezzo_vendita):
        
        self.nome = nome
        self.costo_produzione = costo_produzione
        self.prezzo_vendita = prezzo_vendita
    
    def calcola_profitto(self):
       return self.prezzo_vendita - self.costo_produzione 
    
    def stampa_info(self):
        return f"{self.nome}: Costo produzione: ${self.costo_produzione}, Prezzo di vendita: ${self.prezzo_vendita}"
    

class Automotive(Prodotto):

    def __init__(self, nome, costo_produzione, prezzo_vendita, garanzia):

        self.nome = nome
        self.costo_produzione = costo_produzione
        self.prezzo_vendita = prezzo_vendita
        self.garanzia = garanzia
    
    def stampa_info(self):

        return f"{self.nome}: Costo produzione: ${self.costo_produzione}, Prezzo di vendita: ${self.prezzo_vendita}, Garanzia anni: {self.garanzia}"


class Vestiario(Prodotto):

    def __init__(self, nome, costo_produzione, prezzo_vendita, tessuto):

        self.nome = nome
        self.costo_produzione = costo_produzione
        self.prezzo_vendita = prezzo_vendita
        self.tessuto = tessuto
    
    def stampa_info(self):
        return f"{self.nome}: Costo produzione: ${self.costo_produzione}, Prezzo di vendita: ${self.prezzo_vendita}, Tessuto: {self.tessuto}"
    

class Fabbrica:
    def __init__(self):
         self.inventario = {}
        
    def aggiungi_prodotto(self, prodotto, quantità):

        #controllo se il prodotto è già esistente nell'inventario
        if prodotto.nome in self.inventario:
            #se il prodotto già esiste viene incrementata la quantità
            self.inventario[prodotto.nome]["quantità"] += quantità
        
        #se non presente si aggiunge al dizionario inventario, la chiave è il nome del prodotto, il valore è un altro dizionario contenete il prodotto e la quantità
        else:
            self.inventario[prodotto.nome] = {"prodotto": prodotto, "quantità": quantità}
            print(f"Aggiunti {quantità} pezzi di {prodotto.nome} all'inventario.")

    def vendi_prodotto(self, nome_prodotto, quantità):

        #verifica se il prodotto è nell'inventario. 
        prodotto_info = self.inventario.get(nome_prodotto)
        
        #se presente il prodotto
        if prodotto_info:

            #estrae la quantità disponibile dall'inventario
            quantità_disponibile = prodotto_info["quantità"]

            #controlla se la quantità è disponibile
            if quantità_disponibile >= quantità:
                
                #se disponibile ne riduce la quantità e ne calcola il profitto
                prodotto_info["quantità"] -= quantità
                profitto = prodotto_info["prodotto"].calcola_profitto() * quantità
                print(f"Venduti {quantità} pezzi di {nome_prodotto}. Profitto totale: ${profitto}")
           
            else:
                print(f"Quantità insufficiente per {nome_prodotto}. Disponibili: {quantità_disponibile}")
        else:
            print(f"Il prodotto {nome_prodotto} non esiste nell'inventario.")

    
    def resi_prodotto(self, nome_prodotto, quantità):

        #controlla se il prodotto è disponibili dall'inventario
        if nome_prodotto in self.inventario:

            #se presente riduce la quantità del prodotto reso
            self.inventario[nome_prodotto]["quantità"] += quantità
            print(f"Aumento della quantità di {nome_prodotto} di {quantità} pezzi")
        else:
            print(f"Il prodotto {nome_prodotto} non esiste nell'inventario.")


    def stampa_inventario(self):

        #controlla se l'inventario è vuoto
        if not self.inventario:
            print("L'inventario è vuoto.")

        else:
            print("Inventario:")

            #ciclio per i prodotti dell'inventario
            for nome, info in self.inventario.items():
                prodotto = info['prodotto']
                quantità = info['quantità']
                print(f"{prodotto.stampa_info()} - Quantità disponibile: {quantità}")


def test_fabbrica():

    # Creazione dei prodotti
    auto = Automotive("Audi A6", 20000, 60000, 5)
    camicia = Vestiario("Camicia Slim Fit", 10, 40, "Lino")

    # Creiamo la fabbrica
    fabbrica = Fabbrica()

    # Aggiungiamo i prodotti all'inventario
    fabbrica.aggiungi_prodotto(auto, 10)
    fabbrica.aggiungi_prodotto(camicia, 50)

    # Stampa l'inventario
    fabbrica.stampa_inventario()

    # Vendiamo dei prodotti
    fabbrica.vendi_prodotto("Audi A6", 3)
    fabbrica.vendi_prodotto("Camicia Slim Fit", 25)

    # Stampa l'inventario dopo le vendite
    fabbrica.stampa_inventario()

    # Gestiamo un reso
    fabbrica.resi_prodotto("Camicia Slim Fit", 3)

    # Stampa l'inventario finale
    fabbrica.stampa_inventario()

test_fabbrica()