
#verifica se inizia con ci
stringa = "ciao a tutti"
print(stringa.startswith("ci"))

#verifica se finisce
print(stringa.sendswith("tutti"))

#verifica che ci sono solo caratteri alfanumerici (no spazi, sono caratteri speciali, si a ciao11)
print(stringa.isalnum())

#verifica solo caratteri alfabetici
print(stringa.isalpha())

#verificare se solo solo numeri
print(stringa.isdecimal())

numero=input("inserisci numero: ")
if numero.isdecimal():
    print(int(numero)+5)
else:
    print("non hai inserito il numero!")

# devo salvare in una variabile per fare il replace
stringa = stringa.replace("tutti","nessuno")

#conte quante t ci sono
print(stringa.count("t"))

# al posto della visgola ci saranno i trattini
listas = ["ciao","a","tutti"]
separatore = "-"

stringa = separatore.join(listas)
print(stringa)

# se voglio verificare che la stringa sia presente in lista
if "ciao" in listas:
    print("presente")

#creare una lista di parole che non contengono la lettera a
lista2 = ["ciao","a","tutti","arrivederci","rosso","nero"]

lista3 = []

for elemento in lista2:
    if "a" in elemento:
        pass
    else:
        lista3.append(elemento)

# più breve: se parola è nella lista inserisci parola nella lista (?)
# 1 (parola) elemento che metto nella lista

lista4 = [parola for parola in lista2 if "a" not in parola]




