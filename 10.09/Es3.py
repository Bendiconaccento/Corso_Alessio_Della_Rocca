# Scrivete un programma che prenda i nomi degli alunni di una
# classe e i loro voti, quando l’utente scrive media il programma
# andrà a stampare i nomi di tutti gli alunni e per ogni alunno la
# media dei voti.
# Esempio:
# Nome: Giovanni , Media: 7.5
# Nome: Alfredo , Media: 9
# Nome: Michela, Media 10

# Dizionario per i nomi (chiavi) e i voti
alunni = {}

# Si interrompe solo se inserisco "media"
while True:
    
    nome = input("Inserisci il nome dell'alunno (o scrive 'media' per la media dei voti): ")
    
    if nome.lower() == "media":
        print("Media dei voti per ciascun alunno: ")

        # items() restituisce coppie di chiavi e valori del dizionario
        for nome, voti in alunni.items():
            media_voto = sum(voti) / len(voti)
            print(f"Nome: {nome}, Media: {media_voto}")
        break
    
    voti = input(f"Inserisci i voti di {nome} separati da una virgola: ").split(',')

    voti_convertiti = []

    for voto in voti:
        voti_convertiti.append(float(voto))

    # chiave (nome) valore (voti_convertiti)
    alunni[nome] = voti_convertiti    
    

   
    


