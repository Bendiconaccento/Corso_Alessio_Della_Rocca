#Scrivete un programma che chiede all'utente una
#frase e restituisce solo le vocali e l’indice della
#vocale all’interno della frase.


frase = input("Inserisci una frase: ")

vocali = "aeiouAEIOU"

indice = 0
for carattere in frase:
    if carattere in vocali:
        print(f"Vocale: {carattere} - Indice: {indice}")
    indice += 1

lista = [carattere for carattere in frase if carattere in vocali]
print(lista)


