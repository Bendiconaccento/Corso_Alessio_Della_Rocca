
def calcola_parole(file_path):
    with open(file_path, "r") as file : 
        contenuto = file.read()
        contenuto1 = contenuto.replace("\n", " ")
        contenuto2 = contenuto.replace() 
        numero_caratteri = len(contenuto1)#conta i caratteri
        numero_righe = len(contenuto.splitlines())
        numero_parole = len(contenuto.split())

        print(f"Il numero di caratteri è {numero_caratteri}")
        print(f"Il numero di righe è {numero_righe}")
        print(f"Il numero di parole è {numero_parole}")
        

calcola_parole("testo.txt")