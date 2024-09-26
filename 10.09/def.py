
#se non gli passo niente in somma(), mi chiede di inserire un valore (di default). Se in somma() inserisco "ciao" mi stampa ciao
def somma(stringa = 0):
    if stringa == 0:
        stringa = input("inserisci valore: ")
    print(stringa)

somma()

# puoi utilizzare un un valore di default ma solo al secondo argomento
def somma(a, b=0):
    print(a+b)

somma(4)

# return per trasportare dallo spazio locale allo spazio globale
def somma(a, b=0):
    return a+b
somma1 = somma(4,5)

somma(4,5)

# global per restituire una variabile locale nello spazio globale
def somma():
    global variabile
    variabile = 5 + 5

somma()
print(variabile)

#problema perché argomento in più nonostante i default
def somma(a=0, b=0, c=0):
    print(a+b+c)

somma(1,2,3,4)

#per risovere il problema (utilizza solo il primo argomento se gli metto [0] dopo il print):
def somma(*argomenti):
    print(argomenti)

somma(1,2,3,4)

#oppure: (traformando gli argomenti in dizionario, in queto caso sto richiamamndo la chiave nome)
def somma(**argomenti):
    print(argomenti["nome"])

somma(nome="Tommaso", cognome="Muraca")


def funz1(**argomenti):
    print(argomenti[0])

somma(nome="Tommaso", cognome="Muraca")



