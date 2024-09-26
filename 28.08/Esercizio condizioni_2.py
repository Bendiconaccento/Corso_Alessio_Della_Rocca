x = input("Inserisci una stringa: ")
scelta = int(input("Seleziona un'azione (1-3): ")) # la funzione input() restituisce sempre una stringa se non converti la variabile "scelta" in un numero int()

if scelta == 1:
    op_1 = input("inserisci la stringa da aggiungere: ")
    print("La stringa è stata aggiunta", x, op_1)  # se al posto della "," metti il "+" non ci sarà lo spazio tra le due parole. Con il "+" sarebbe una concatenazione

elif scelta == 2:
    op_2 = input("Inserisci la modifica: ")
    print("la stringa è stata modificata")
    print(op_2)

elif scelta == 3:
    op_3 = input("Inserisci la stringa da rimuovere: ")
    x= x.replace(op_3, "")                         # x.replace(op_3, "") rimuove tutte le parole di op_3 dalla stringa x. (perchè sostituisce la parola  di op_3 con uno spazio vuoto dato da "")
    print("La stringa risultante è: ", x)
    

else:
    print("Nessuna operazione valida")

