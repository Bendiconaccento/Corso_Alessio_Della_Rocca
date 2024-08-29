
lista = input("Inserire una lista di numeri separati da uno spazio: ")

# lista di stringhe
lista_split = lista.split()

# trasformare in interi
n = [int(x) for x in lista_split]
print(n)

# condizione per verificare se la lista è vuolta
if len(n) == 0:
    print("Lista Vuota")
else:
    # inizializziamo il massimo come il primo elemento della lista (n)
    massimo = n[0]

    # si compara il primo numero [n(0)] con tutti i numeri successivi della lista
    for i in n:

        # se il numero corrente è maggiore del massimo attuale si aggiorna il massimo (sennò va avanti)
        if i > massimo:
            massimo = i


    # inizializziamo un contatore (conta il numero di elementi)
    count = 0

    # inizializziamo una variabile (i) per rappresentare l'indice corrente nella lista (parte dal primo elemento)
    i = 0

    # while scorre la lista elemento per elemento
    while True:

        # se l'indice (i) supera o è uguale alla lunghezza della lista si esce dal ciclo
        if i >= len(n):
            break
        count += 1  # incrementa il contatore per ogni elemento 
        i += 1      # passa al prossimo elemento

print(massimo)
print(count)