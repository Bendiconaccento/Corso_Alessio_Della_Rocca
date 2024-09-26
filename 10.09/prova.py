

# lista = ["ciao","a","tutti", 8, 8.88, [1,2,3]]
# print(lista)
# print(lista.index("ciao"))

# lista2 = [4,5,6]

# #aggiungo alla coda della lista i numeri della lista 2
# lista.extend(lista2)

# # ordina in ordine decrescente
# lista2.sort(reverse=True)

# lista.pop(2)

# # evita il contatore
# for indice, valore in enumerate(lista):
#     print(f"indice: {indice}, valore: {valore}")

#stringa = "ciao-a-tutti"
# ti dice con cosa inizia, endswith con cosa finisce
#print(stringa.startswith("ciao"))

#lista = stringa.split("-")

#print(lista[0])

# join trasforma una lista di stringhe in una lista, da utilizzare solo se nella lista c'è una stringa
#lista = ["ciao","a","tutti"]
#stringa = "-".join(lista)

#print(stringa)


'''''
lista = [1,2,3, "ciao"]
lista2 = []

for element in lista:
    lista2.append(str(element))

print(lista2)

'''''

lista = [1,2,3,4,5]

tupla = (1,2,3,4,5)

# non printa i duplicati
set = {1,2,3,4,5, 5,5}

# diozionari
tommaso = {"nome":"tommaso","cognome":"muraca","ruolo":"formatore"}

mirko = {"nome":"mirko","ruolo":"formatore"}

utenti = {}

utenti[0]=tommaso
utenti[1]=mirko

utenti = {0: {'nome':"tommaso","cognome":"muraca","ruolo":"formatore"},
          1: {'nome':"mirko","ruolo":"formatore"}} 

# .get permette di specificare un valore predefinito da restituire se la chiave non esiste. Questo evita che si verifichino errori, 
# come un KeyError, quando si tenta di accedere a una chiave non presente.
for chiave in utenti:
    print(utenti[chiave].get("cognome","cognome non presente"))

# .keys ci restituisce tutte le chiavi, .values i valori

# tupla di tutti gli elementi
# utentiItems = utenti[0].items()
# print(utentiItems)

# utente1 = utenti[0]

# print(utente1.setdefault("indirizo","indirizzo non presente"))

# print(utente1)
