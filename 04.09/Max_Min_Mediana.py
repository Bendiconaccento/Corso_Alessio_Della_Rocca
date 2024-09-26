#Create un programma che genera una lista da 10 input dell'utente, dovrà restituire il numero medio (in mezzo), il numero massimo e il numero minimo

numeri = input("Inserisci 10 numeri separati da uno spazio: ")

# crea una lista di stringhe
n_split = numeri.split()

# converte le stringhe in numeri interi
n = [int(x) for x in n_split]

# inizializziamo il massimo come primo elemento della lista
massimo = n[0]

# se il maggiore corrente è maggiore del massimo attuale si aggiorna il massimo (sennò prosegue)
for i in n:
    if i > massimo:
        massimo = i
        
print(f"Il massimo è: {massimo}")

minimo = n[0]
for i in n:
    if i < minimo:
        mminimo = i

print(f"Il minimo è: {minimo}")


# ordino la lista
n.sort()

# lunghezza lista (10) numero di elementi
l_n = len(n)

# dispari
if l_n % 2 == 1:
    mediana = n[l_n//2]

# pari
else:
    mediana = (n[l_n//2-1] + n [l_n//2])/2

print(mediana)