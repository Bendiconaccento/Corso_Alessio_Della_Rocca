
# Definizione delle funzioni
def area_triangolo(base, altezza):
    return (base * altezza) / 2

def area_quadrato(lato):
    return lato ** 2

def area_rettangolo(base, altezza):
    return base * altezza

# Inizializzazione di una lista vuota per i risultati delle aree
aree = []

# Ciclo di scelta
while True:
    print("Scegli la figura di cui vuoi calcolare l'area: ")
    print("1. Triangolo")
    print("2. Quadrato")
    print("3. Rettangolo")
    print("4. Esci e mostra i risultati")

    scelta = input("Inserisci il numero della figura: ")

    if scelta == "1":
        base = int(input("Inserisci la base del triangolo: "))
        altezza = int(input("Inserisci l'altezza del triangolo: "))
        area = area_triangolo(base, altezza)
        aree.append(("Triangolo",area))                 # Tupla con 2 elementi (grazie Nicola*)
        print(f"L'area del trinagolo è: {area}")
    
    elif scelta == "2":
        lato = int(input("Inserisci il lato del quadrato: "))
        area = area_quadrato(lato)
        aree.append(("Quadrato",area))
        print(f"L'area del quadrato è: {area}")
    
    elif scelta == "3":
        base = int(input("Inserisci la base del rettangolo: "))
        altezza = int(input("Inserisci l'altezza del rettangolo: "))
        area = area_rettangolo(base, altezza)
        aree.append(("Rettangolo",area))
        print(f"L'area del rettangolo è: {area}")
    
    elif scelta == "4":

        # *Il ciclo decompone la tupla presente in aree
        for figura, area in aree:
            print(f"{figura}: {area}")

        break
    
    else:
        print("Scelta non valida. Riprova.")


