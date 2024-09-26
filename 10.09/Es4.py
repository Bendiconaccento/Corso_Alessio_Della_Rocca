
#Scrivete un programma che utilizza una funzione che accetta
# come parametro una stringa passata dall’utente e restituisce in
# risposta se è palindroma o no.
# Esempio:
# ‘I topi non avevano nipoti’ è palindroma
# 'ciao' non è palindroma


def verifica_palindromo(stringa):
    stringa_pulita = stringa.replace(" ","").lower()

    if stringa_pulita == stringa_pulita[::-1]:      #legge tutta la sequenza da inizio (:) a fine (:) ma al contrario (-1)
        return True
    else:
        return False
    

def utente():

    stringa_utente = input("Inserisci una stringa: ")

    if verifica_palindromo(stringa_utente):
        print(f"{stringa_utente} è palindroma")
    
    else:
        print(f"{stringa_utente} non è palindroma")


utente()
    


# oppure per rigirare la frase:

stringa1 = "ciao a tutti"
stringa2 = ""

for i in range(len(stringa1)-1, -1, -1):
    stringa2 += stringa1[i]

print(stringa2)


