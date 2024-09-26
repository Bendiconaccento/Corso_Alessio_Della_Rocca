
#Scrivete una programma che richiede una lista di numeri all’utente e
#fornisce in output un istogramma basato su questi numeri, usando asterischi
#per disegnarlo.

#METODO 1
numeri = input("Scrivi una lista di numeri separati da uno spazio: ")

# crea una lista di stringhe
n_split = numeri.split()

# converte le stringhe in numeri interi
n_conv = [int(x) for x in n_split]

for i in n_conv:
    print (i * "*")




# METODO 2
n = int(input("Quanti numeri vuoi inserire?"))

lista = []

for i in range(n):
    numeri = int(input("Inserisci i numeri: "))
    lista.append(numeri)


for i in lista:
    string =""
    for elemento in range (i):
        string += "*"
    print(string)