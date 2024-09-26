
#open accetta 2 valori: nome file e il modo in cui intendiamo gestire il file: read (r), write, x (creare un nuovo file)

#read legge un file ma se non è presente da errore
# write lo sovrascrive se presente


# def lettura_file():
#     with open("prova.txt","r") as myfile:
#         contenuto = myfile.read()

# with open("prova.txt", "a") as myfile:
#     myfile.write("prima riga")

# #METTE LA SECONDA RIGA IN PROVA.TXT  \n
# #with open("prova.txt", "a") as myfile:
#     #myfile.write("\nprima riga")


# def scrittura_file():
#     with open("prova.txt", "a") as myfile:
#         myfile.write("prima riga")

# def lettura_file():
#     with open("prova.txt","r") as myfile:
#         contenuto = myfile.readlines()
#         print(contenuto)

# def scrittura_file():
#     with open("prova.txt", "a") as myfile:
#         myfile.write("\nprima riga")
    

# # se voglio utilizzare un contenuto esterno devo fare un return
# # senza def non serve perché non sono interno
# def lettura_file():
#     with open("prova.txt","r") as myfile:
#         contenuto = myfile.read()
#         return contenuto

# lettura_file("test.csv")

# contenuto = lettura_file("test.txt")

# # per richiamare un contenuto del csv

# righe = contenuto.split("\n")

# print(righe)

# #oppure

# for i in range(1, len(righe)):
#     print(righe[i].split,(",")[0])

# invece di leggere i nomi volessi aggiungere una riga ecc.

#SE LAVORO DENTRO IL WITH APRO E CHIUDO IL FILE

# nome = "alfredo"
# cognome = "verdi"
# via = "via milano"

# stringa = nome + "," + cognome + "," + via

# scrittura_file("testCsv.txt", stringa)


def scrittura_file():
    with open("provaCsv.txt", "a") as myfile:
        myfile.write("prima riga")