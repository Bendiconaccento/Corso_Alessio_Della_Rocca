
n =input("Inserisci i numeri separati da uno spazio: ")

# come capire in tipo di variabile
if type(n) == str:
    print("n è una stringa")
else:
    print("n non è una stringa")

# crea una lista di stringhe
n_split = n.split()

# converte le stringhe in numeri interi
n_conv = [int(x) for x in n_split]

# ciclo per calcolare il quadrato di ciascun numero
for i in n_conv:
   print(i**2)


