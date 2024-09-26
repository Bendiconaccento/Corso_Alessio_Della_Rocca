# Scelta dei numeri
n_1= int(input("Inserisci il primo numero: "))
n_2= int(input("Inserisci il secondo numero: "))

# Scelta dell'operazione
scelta = int(input("Scegli l'operazione da fare (1-4): "))


if scelta == 1:
    print(n_1 + n_2)

elif scelta == 2:
    print(n_1-n_2)

elif scelta == 3:
    print(n_1*n_2)

elif scelta == 4 and n_2 != 0:        #se il n_2 è = zero -> messaggio errore
    print(n_1/n_2)

else:
    print("Errore: Divisione per zero")

if scelta != 1 or 2 or 3 or 4:        # se sceglie != da 1 a 4 -> operazione non valida
   print("Operazione non valida")


        



