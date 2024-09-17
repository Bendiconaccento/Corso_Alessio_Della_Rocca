
import numpy as np

def creazione_matrice():

    righe = int(input("Inserire il numero di righe: "))
    colonne = int(input("Inserire il numero di colonne: "))

    matrice = np.random.rand(righe,colonne)
    print(matrice)
    return matrice


def estrai_sottomatrice(matrice):

    #dimensioni matrice
    righe, colonne = matrice.shape

    #calcola indice centrale 
    centro_riga = righe // 2
    centro_colonna = colonne // 2

    #calcola indice di partenza e fine per la sottomatrice. Inizia una riga sopra il centro
    inizio_riga = max(0, centro_riga -1)
    #prende una riga sotto il centro senza andare oltre il numero totale
    fine_riga = min(righe, centro_riga +2)

    inizio_colonna = max(0, centro_colonna -1)
    fine_colonna = min(colonne, centro_colonna +2)

    #uso dello slicing per estrarre la sottomatrice
    sottomatrice = matrice[inizio_riga:fine_riga, inizio_colonna:fine_colonna]

    print(sottomatrice)


def trasposta_matrice(matrice):

    trasposta = np.transpose(matrice)
    print(trasposta)


def somma_elementi(matrice):

    somma = np.sum(matrice)
    print(somma)


def menu():

    matrice = None

    while True:

        print("1. Crea una nuova matrice")
        print("2. Estrarre e stampare la sottomatrice")
        print("3. Trasponi la matrice")
        print("4. Somma degli elementi della matrice")
        print("5. Uscire")

        scelta = input("Scegli una opzione: ")

        if scelta == "1":
            matrice = creazione_matrice()

        elif scelta == "2":
            if matrice is not None:
                estrai_sottomatrice(matrice)
            else:
                print("Devi prima creare una matrice")
        
        elif scelta == "3":
            if matrice is not None:
                trasposta_matrice(matrice)
            else:
                print("Devi prima creare una matrice")
        
        elif scelta == "4":
            if matrice is not None:
                somma_elementi(matrice)
            else:
                print("Devi prima creare una matrice")
        
        elif scelta == "5":
            print("Uscita dal programma")
            break
            
        else:
            print("Scelta non valida, riprovare")
    
menu()