# Scrivete un programma che chiede un numero all’utente e
# restituisce un dizionario con il quadrato del numero, se è pari o
# dispari e quante cifre contiene.
# Esempio:
# Numero 12
# Risultato
# {‘quadrato’: 144,’pari o dispari’:’pari’, ‘n. cifre’: 2 }


numero = int(input("Inserisci un numero: "))

quadrato = numero ** 2

if numero % 2 == 0:
     x = "pari"

else:
     x = "dispari"

cifre = len(str(numero))

dizionario = {
     "quadrato": quadrato,
     "pari o dispari": x,
     "n. cifre": cifre
}

print(dizionario)
