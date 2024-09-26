# Creare il file in formato txt con nome ProvaCsv.txt
with open("ProvaCsv.txt", "w") as file:
    file.write("Nuova riga.\n")
    file.write("Altra riga.")


#Puoi aprire il file in modalità append per aggiungere contenuto alla fine del file, senza sovrascriverlo
def append_to_file(file_name, content):
    with open(file_name, "a") as file:
        file.write(content + "\n")

# Esempio di utilizzo
append_to_file("ProvaCsv.txt", "Aggiunta di una nuova riga di testo.")

