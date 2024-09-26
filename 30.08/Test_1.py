
# inizializzazione di una lista
lista = []

# richiesta all'utente del numero di parole
n_parole = int(input("quante parole vuoi aggiungere alla lista?: "))

# ciclo per far inserire le parole dall'utente
for i in range(n_parole):
    parola = input("inserisci parola: ")

    # aggiunge le parole alla lista
    lista.append(parola)

print(lista)