# stampa lista + lista_2
lista=[1,2,3]

lista_2=[4,5,6]

lista.extend(lista_2)

print(lista)

#mette dove vogliamo noi il dovici (posizione 0)
lista.insert(0,"dodici")
print(lista)

#modifica la lista ma non restituisce valore
#print(lista.sort())

#più grande al più piccolo
#lista.sort(reverse=True)
#print(lista)

lista_1=[55,1,2,3]

#cercami quella cosa e fai break. Stampa posizione 0
print(lista_1.index(55))

#eliminare un elemento nella lista
print(lista_1.remove(55))

#toglie l'ultimo elemento in assoluto
lista_1.pop()

#se gli passo l'indice va ad eliminare quel valore nella posizione 0
print(lista_1.pop(0))

#elimina la lista o gli elementi della lista
# del lista
# del lista[0]

#sostituire un elento nella lista. Restiuisce la lista dove c'è 0 al posto del 55
lista_1[0]=0



#creare una lista di parole che non contengono la lettera a
lista2 = ["ciao","a","tutti","arrivederci","rosso","nero"]

lista3 = []

for elemento in lista2:
    if "a" in elemento:
        pass
    else:
        lista3.append(elemento)