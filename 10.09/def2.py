

def pari_dispari(n):
    if n%2 == 0:
        return True
    else:
        return False
    

lista = [1,2,3,4,5,6]

#inserisci il numero, per ogni numero in lista controlla se pari
listapari = [n for n in lista if pari_dispari(n)]

print(listapari)


#oppure:
listapari2 = list(filter(pari_dispari, lista))

print(listapari2)


def triplica(n):
    return n*3

listaT = [triplica(n) for n in lista]

print(listaT)


# gli dai la funzione e l'argomento su cui vuoi iterare l'operazione triplica (lista) - (prima lo devi trasformare il lista)
listaT2 = list(map(triplica, lista))
print(listaT2)