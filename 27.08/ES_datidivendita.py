
def inserimento_dati ():
    
    while True:
        vendite = input("Inserisci una serie di importi di vendita separati da uno spazio (oppure 'q' per uscire): ")
        
        if vendite.lower() == 'q':  # Opzione per uscire dal ciclo
            break
        
        try:
            # Convertire gli input in una lista di numeri
            vendite_lista = [float(v) for v in vendite.split()]
            print(f"Importi di vendita inseriti: {vendite_lista}")
        except ValueError:
            print("Errore: assicurati di inserire solo numeri separati da uno spazio.")
