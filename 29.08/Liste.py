numeri = [1,2,3,4,5]
nomi = ["Alice","Bob","Alessio"]
misto = [1,"due", True, 4.5]

print(numeri[0])
print(numeri[2])
print(misto[2])

numeri[2]=10     #modifica della lista: numero 2 diventa 10
print(numeri)

numeri = [3,1,4,2,5]
print(len(numeri))     #lunghezza lista

numeri.append(8)       #aggiunge un elemento alla fine della lista
print(numeri)

numeri.insert(2, 10)   #inserire un elemento in una specifica posizione
print(numeri)

numeri.remove(4)       #rimuove un elemento (il numero 4)
print(numeri)

numeri.sort()          #ordinare gli elementi
print(numeri)

