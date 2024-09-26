
class Ristorante:

    def __init__(self, nome, tipo_cucina):      # Metodo costruttore

        self.nome = nome                        # Attributo di istanza
        self.tipo_cucina = tipo_cucina          # Attributo di istanza
        self.aperto = False                     # Ristorante chiuso di default
        self.menu = {}                          # Dizionario per memorizzare prezzi e piatti del ristorante

    def descrivi_ristorante(self):
        print(f"Il nome del ristorante è {self.nome}, il tipo di cucina è {self.tipo_cucina}")

    def stato_apertura(self):

        if self.aperto:
            print(f"Il ristornate {self.nome} è aperto")
        else:
            print(f"Il ristorante {self.nome} è chiuso")
    
    def apri_ristorante(self):
        self.aperto = True
        print(f"Il ristorante {self.nome} è aperto")
    
    def chiudi_ristorante(self):
        self.aperto = False
        print(f"Il ristorante {self.nome} è chiuso")
    
    def aggiungi_al_menu(self, piatto, prezzo):
        self.menu[piatto] = prezzo      # piatto = chiave ; = prezzo: assegna prezzo alla chiave piatto
        print(f"Il piatto {piatto} è stato aggiunto al menù con il prezzo di {prezzo} ")

    def togli_dal_menu(self, piatto):

        if piatto in self.menu:
            del self.menu[piatto]       # del: per rimuovere un oggetto
            print(f"Il piatto {piatto} è stato rimosso dal menù")
        
        else:
            print(f"Il piatto {piatto} non è presente nel menù")

    def stampa_menu(self):

        for piatto, prezzo in self.menu.items():
            print(f"{piatto}: ${prezzo}")

    # print(menu vuoto)  

        
